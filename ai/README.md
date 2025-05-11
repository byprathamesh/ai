# Health Insurance Premium AI (Vercel-ready)

- Upload a blood test report (PDF or image)
- Instantly see insurance eligibility and premium
- Powered by Python AI backend and Next.js frontend
- Deployable to Vercel

## How to use locally

1. Install Node.js and Python 3.9+
2. `npm install`
3. `pip install -r api/requirements.txt`
4. `npm run dev`
5. Open http://localhost:3000

## Deploy to Vercel

- Push to GitHub and import to Vercel
- Vercel will auto-detect Next.js and Python API 

## 🚀 New Features & Improvements

- **Better OCR**: Uses PaddleOCR (optional, install with `pip install paddleocr`) for improved image extraction.
- **Machine Learning Ready**: Scaffold for training ML models with scikit-learn/XGBoost in `api/train_model.py`.
- **Testing**: Unit tests for extractors in `tests/` (run with `pytest`).

## 🚀 New Advanced Features

- **Multiple Datasets:** Easily switch between heart disease and diabetes datasets (see `api/train_model.py`).
- **Model Options:** Train with RandomForest or XGBoost (if installed).
- **Hyperparameter Tuning:** Uses GridSearchCV for best model selection.
- **Experiment Tracking:** Integrates with Weights & Biases (wandb) for free experiment tracking and visualization (optional, install with `pip install wandb`).

## 📊 Free Datasets for Training
- [Hugging Face Datasets](https://huggingface.co/datasets)
- [Kaggle Health Datasets](https://www.kaggle.com/datasets)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)
- [MIMIC-III (clinical data, requires credential)](https://physionet.org/content/mimiciii/1.4/)

## 🧑‍💻 Training a Model
- See `api/train_model.py` for a scaffold to train your own model.
- Place your data in a `data/` folder and update the script.
- Save your trained model and load it in the API for predictions.

## 🧑‍💻 Training a Model (Advanced)
- Edit `api/train_model.py` to set `DATASET` and `MODEL_TYPE`.
- Run: `python ai/api/train_model.py`
- The best model will be saved in `data/` with the dataset and model type in the filename.

## 📊 Adding More Datasets
- Download any CSV from Kaggle, UCI, or Hugging Face and add it to the `data/` folder.
- Update `DATASETS` in `api/train_model.py` to add your new dataset.

## 🛡️ Privacy & Data Handling
- Uploaded files are processed in memory and deleted after extraction.
- No data is stored unless you modify the code to do so.

## 📝 How to Add New Metrics
- Edit the regexes in `api/extractors/pdf_extractor.py` and `api/extractors/image_extractor.py`.
- Add new rules in `api/rules/premium_rules.py`.

## 🧪 Running Tests
- Install dev dependencies: `pip install -r api/requirements.txt`
- Run tests: `pytest tests/`
- Run: `python -m pytest tests/` 