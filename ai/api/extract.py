import sys
import os
import tempfile
from extractors.pdf_extractor import extract_metrics_from_pdf
from extractors.image_extractor import extract_metrics_from_image
from rules.premium_rules import evaluate_customer

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
        result = evaluate_customer(metrics)
        import json
        return Response(json.dumps({"metrics": metrics, "result": result}), mimetype="application/json")
    finally:
        os.remove(temp_path) 