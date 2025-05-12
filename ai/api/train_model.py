# train_model.py
# Advanced training script: supports multiple datasets, models, experiment tracking, and hyperparameter tuning.

import os
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Optional: XGBoost
try:
    from xgboost import XGBClassifier
except ImportError:
    XGBClassifier = None

# Optional: Weights & Biases
try:
    import wandb
    WANDB_AVAILABLE = True
except ImportError:
    WANDB_AVAILABLE = False

# DATASET OPTIONS
DATASETS = {
    'heart': {
        'url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data',
        'path': 'data/heart.csv',
        'columns': [
            'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
            'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'
        ],
        'target_transform': lambda y: (y > 0).astype(int)
    },
    'diabetes': {
        'url': 'https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv',
        'path': 'data/diabetes.csv',
        'columns': None,  # CSV has headers
        'target_col': 'Outcome',
        'target_transform': lambda y: y
    }
}

# Choose dataset and model here
DATASET = 'heart'  # or 'diabetes'
MODEL_TYPE = 'randomforest'  # or 'xgboost'

os.makedirs('data', exist_ok=True)

# Download dataset if not present
dataset_info = DATASETS[DATASET]
if not os.path.exists(dataset_info['path']):
    import urllib.request
    print(f"Downloading {DATASET} dataset...")
    urllib.request.urlretrieve(dataset_info['url'], dataset_info['path'])

# Load data
if DATASET == 'heart':
    df = pd.read_csv(dataset_info['path'], names=dataset_info['columns'])
    df = df.replace('?', pd.NA).dropna()
    df = df.astype(float)
    X = df.drop('target', axis=1)
    y = dataset_info['target_transform'](df['target'])
elif DATASET == 'diabetes':
    df = pd.read_csv(dataset_info['path'])
    X = df.drop('Outcome', axis=1)
    y = dataset_info['target_transform'](df['Outcome'])
else:
    raise ValueError('Unknown dataset')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model selection
if MODEL_TYPE == 'randomforest':
    model = RandomForestClassifier(random_state=42)
    param_grid = {'n_estimators': [100, 200], 'max_depth': [None, 5, 10]}
elif MODEL_TYPE == 'xgboost' and XGBClassifier is not None:
    model = XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss')
    param_grid = {'n_estimators': [100, 200], 'max_depth': [3, 5, 10]}
else:
    raise ValueError('Unknown or unavailable model type')

# Hyperparameter tuning (GridSearchCV)
gs = GridSearchCV(model, param_grid, cv=3, n_jobs=-1)
gs.fit(X_train, y_train)
model = gs.best_estimator_

# Experiment tracking with Weights & Biases
if WANDB_AVAILABLE:
    wandb.init(project='health-insurance-ai', config={
        'dataset': DATASET,
        'model': MODEL_TYPE,
        'best_params': gs.best_params_
    })
    try:
        y_pred = model.predict(X_test)
        try:
            y_probas = model.predict_proba(X_test)
        except Exception:
            y_probas = None
        if y_probas is not None:
            wandb.sklearn.plot_classifier(gs, X_train, X_test, y_train, y_test, y_pred, y_probas, labels=[0, 1], model_name=MODEL_TYPE)
    except Exception as e:
        print(f"wandb plot_classifier failed: {e}")
    wandb.finish()

print(classification_report(y_test, y_pred))

joblib.dump(model, f'data/model_{DATASET}_{MODEL_TYPE}.joblib')
print(f'Model trained and saved to data/model_{DATASET}_{MODEL_TYPE}.joblib') 