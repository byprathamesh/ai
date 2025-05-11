import sys
import os
import tempfile
from extractors.pdf_extractor import extract_metrics_from_pdf
from extractors.image_extractor import extract_metrics_from_image
from rules.premium_rules import evaluate_customer

# Try to load the ML model if available
model = None
model_features = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
    'exang', 'oldpeak', 'slope', 'ca', 'thal'
]
try:
    import joblib
    model = joblib.load('data/model.joblib')
except Exception:
    pass

def handler(request):
    from werkzeug.wrappers import Request, Response
    req = Request(request)
    file = req.files.get('file')
    if not file:
        return Response("No file uploaded", status=400)
    ext = os.path.splitext(file.filename)[1].lower()
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as temp:
        temp.write(file.read())
        temp_path = temp.name
    try:
        if ext == ".pdf":
            metrics = extract_metrics_from_pdf(temp_path)
        else:
            metrics = extract_metrics_from_image(temp_path)
        # Try ML model if available and all features are present
        ml_result = None
        if model is not None and all(f in metrics for f in model_features):
            import numpy as np
            X = np.array([[metrics[f] for f in model_features]])
            pred = model.predict(X)[0]
            ml_result = {'eligible': bool(pred), 'source': 'ml_model'}
        # Fallback to rules
        result = ml_result if ml_result is not None else evaluate_customer(metrics)
        import json
        return Response(json.dumps({"metrics": metrics, "result": result}), mimetype="application/json")
    finally:
        os.remove(temp_path) 