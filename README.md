# ScoreSense — Student Performance Prediction

ScoreSense is an end-to-end machine-learning application that estimates a student's mathematics score from academic, demographic, and preparation-related information.

It includes a Flask web application, reusable training and inference components, exploratory notebooks, and serialized model artifacts.

> Predictions are estimates for educational exploration. They are not official grades or definitive evaluations of a student.

## Features

- Landing page at `/`
- Prediction form at `/predictdata`
- Health check at `/health`
- Numerical and categorical feature preprocessing
- Model comparison and selection by test R² score
- Saved model and preprocessor artifacts
- Exploratory data analysis and model-training notebooks

The prediction form accepts gender, race or ethnicity, parental education, lunch type, test-preparation status, reading score, and writing score. Reading and writing scores must be between 0 and 100.

## Project structure

```text
.
├── app.py                              # Flask application and routes
├── Dockerfile                          # Container definition
├── pyproject.toml                      # Package metadata and dependencies
├── requirements.txt                    # Pinned dependency list
├── scripts/
│   └── train.py                        # Training workflow entry point
├── src/student_dashboard/
│   ├── component/
│   │   ├── ingestion.py                # Load data and create train/test files
│   │   ├── data_transformation.py      # Build and save preprocessing pipeline
│   │   └── model_trainer.py            # Compare and save the best model
│   ├── pipeline/
│   │   └── predict_pipeline.py         # Inference and input preparation
│   ├── exception.py                    # Custom exception handling
│   ├── logger.py                       # Application logging
│   └── utils.py                        # Serialization and evaluation helpers
├── templates/
│   ├── index.html                      # Landing page
│   └── Home.html                       # Prediction form and result page
├── notebook/
│   ├── EDA.ipynb
│   ├── model_training.ipynb
│   └── data/stud.csv                  # Source dataset
└── artifacts/
    ├── model.pkl                       # Trained model
    └── preprocessor.pkl                # Fitted preprocessor
```

Training also creates `artifacts/data.csv`, `artifacts/train.csv`, and `artifacts/test.csv`; these generated datasets are ignored by Git.

## Machine-learning workflow

1. Read `notebook/data/stud.csv` and create an 80/20 train/test split.
2. Impute missing values, scale numerical features, and one-hot encode categorical features.
3. Compare Linear Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost, CatBoost, and AdaBoost.
4. Select the model with the highest test R² score. Training fails if the best score is below `0.6`.
5. Save the selected model and fitted preprocessor in `artifacts/`.
6. Load those files during prediction and return the estimated mathematics score.

## Requirements

- Python 3.13 or newer
- `pip` or [`uv`](https://docs.astral.sh/uv/)
- Dependencies from `pyproject.toml` or `requirements.txt`

The training code imports CatBoost, so install it before training:

```bash
python -m pip install catboost
```

## Setup

Clone the repository:

```bash
git clone https://github.com/AryanPratap-Singh/End-to-End-Data-Science-project-student_data_management-.git
cd End-to-End-Data-Science-project-student_data_management-
```

Using `uv`:

```bash
uv sync
uv run python -m pip install catboost
```

Using a regular virtual environment:

```bash
python -m venv .venv

# Windows PowerShell
.venv\\Scripts\\Activate.ps1

# macOS/Linux
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
pip install catboost
```

## Train the model

Run this command from the repository root:

```bash
python scripts/train.py
```

It reads the source CSV, creates train/test files, fits the preprocessing pipeline, compares candidate models, and writes:

```text
artifacts/model.pkl
artifacts/preprocessor.pkl
```

The repository already contains inference artifacts. Re-run training whenever the source data or training code changes.

## Run the web application

```bash
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in a browser.

| Route | Method | Purpose |
| --- | --- | --- |
| `/` | GET | Landing page |
| `/predictdata` | GET | Prediction form |
| `/predictdata` | POST | Generate a mathematics-score estimate |
| `/health` | GET | Return the service health status |

## Notebooks

Start Jupyter from the repository root:

```bash
jupyter notebook
```

- [`notebook/EDA.ipynb`](notebook/EDA.ipynb) explores the dataset and feature relationships.
- [`notebook/model_training.ipynb`](notebook/model_training.ipynb) documents experimentation and model training.

## Docker

The included `Dockerfile` exposes port `5000` and starts the application with Gunicorn:

```bash
docker build -t scoresense .
docker run --rm -p 5000:5000 scoresense
```

The Dockerfile expects `gunicorn` to be available in the installed project dependencies. Add it to `pyproject.toml` before building if it is not already available.

## Responsible use

Demographic and socioeconomic fields may reflect historical bias, and model performance may not generalize to other schools or populations. Do not use this prediction as the sole basis for high-impact educational decisions. Load pickle files only from trusted sources.

## Author

**Aryan Pratap Singh**

- GitHub: [@AryanPratap-Singh](https://github.com/AryanPratap-Singh)
- Email: aryansingh87615@gmail.com

