# ScoreSense — Student Performance Prediction

An end-to-end machine-learning project that transforms student assessment data into an interactive web prediction tool. The application estimates a student's mathematics score from academic, demographic, and preparation-related information.

The project demonstrates a complete data-science workflow:

- Exploratory data analysis in Jupyter Notebooks
- CSV data ingestion and train/test splitting
- Numerical and categorical feature transformation
- Model comparison with hyperparameter tuning
- Best-model selection using the R² score
- Model and preprocessor serialization with `pickle`
- Flask-based prediction interface

> **Note:** Predictions are estimates for educational exploration and should not be treated as official grades or definitive evaluations of a student.

## Demo flow

1. Open the ScoreSense landing page.
2. Select the student's profile information.
3. Enter reading and writing scores from 0–100.
4. Submit the form.
5. View the estimated mathematics score.

The web application is served by [`app.py`](app.py), with templates in [`templates/`](templates/).

## Features

- Clean, responsive Flask user interface
- Predictive form for:
  - Gender
  - Race or ethnicity group
  - Parental education level
  - Lunch type
  - Test preparation status
  - Reading score
  - Writing score
- Reusable ingestion, transformation, training, and prediction components
- Logging and custom exception handling
- Model evaluation using R²
- Comparison of several regression algorithms, including:
  - Linear Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - XGBoost
  - CatBoost
  - AdaBoost

## Project structure

```text
.
├── app.py                         # Flask application and prediction routes
├── notebook/
│   ├── EDA.ipynb                  # Exploratory data analysis
│   ├── model_training.ipynb       # Model experimentation and training
│   └── data/stud.csv              # Source student-performance dataset
├── src/student_dashboard/
│   ├── component/
│   │   ├── ingestion.py           # Data loading and train/test split
│   │   ├── data_transformation.py  # Feature preprocessing
│   │   └── model_trainer.py        # Model comparison and training
│   ├── pipeline/
│   │   └── predict_pipeline.py    # Inference pipeline and input preparation
│   ├── exception.py                # Custom exception handling
│   ├── logger.py                   # Application logging
│   └── utils.py                    # Serialization and model evaluation helpers
├── templates/
│   ├── index.html                  # Landing page
│   └── Home.html                   # Prediction form
├── pyproject.toml                  # Project metadata and dependencies
└── artifacts/                      # Generated data, model, and preprocessor files
```

## Tech stack

- **Python 3.13+**
- **Pandas** and **NumPy** for data handling
- **Scikit-learn** for preprocessing, evaluation, and baseline models
- **CatBoost** and **XGBoost** for gradient-boosted regression
- **Flask** for the web application
- **Jupyter Notebook** for analysis and experimentation
- **uv** for environment and dependency management

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/AryanPratap-Singh/End-to-End-Data-Science-project-student_data_management-.git
cd End-to-End-Data-Science-project-student_data_management-
```

### 2. Create an environment and install dependencies

The project declares its dependencies in `pyproject.toml`. Using `uv`:

```bash
uv sync
```

Alternatively, create a regular virtual environment and install the runtime packages:

```bash
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install pandas numpy scikit-learn catboost xgboost flask
```

For notebook work, also install the development dependencies:

```bash
pip install ipykernel seaborn matplotlib
```

### 3. Generate the training artifacts

The application loads the trained model and preprocessor from `artifacts/`. If these files are not already present, run the ingestion/training workflow from the project root:

```bash
python src/student_dashboard/component/ingestion.py
```

This workflow reads `notebook/data/stud.csv`, creates the train/test datasets, transforms the features, evaluates candidate models, and saves the selected model and preprocessor under `artifacts/`.

The expected inference files are:

```text
artifacts/model.pkl
artifacts/preprocessor.pkl
```

### 4. Start the Flask application

```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

## Using the notebooks

The notebooks are useful for understanding the project before running the web app:

- [`notebook/EDA.ipynb`](notebook/EDA.ipynb) explores the source data and its relationships.
- [`notebook/model_training.ipynb`](notebook/model_training.ipynb) documents model experimentation and training.

Start Jupyter from the repository root:

```bash
jupyter notebook
```

## Machine-learning workflow

1. **Ingestion:** Load `stud.csv` and split the data into training and test sets using a fixed random state.
2. **Transformation:** Process categorical and numerical columns using the transformation pipeline.
3. **Evaluation:** Train multiple regression models and search candidate hyperparameters with cross-validation.
4. **Selection:** Select the model with the highest test R² score, subject to the project's minimum score threshold.
5. **Persistence:** Save the selected model and fitted preprocessor as pickle files.
6. **Prediction:** Convert form input into a DataFrame, apply the saved preprocessor, and return the model's mathematics-score estimate.

## Input features

| Feature | Description |
|---|---|
| `gender` | Student gender |
| `race_ethnicity` | Group A–E category |
| `parental_level_of_education` | Parent/guardian education level |
| `lunch` | Standard or free/reduced lunch |
| `test_preparation_course` | None or completed |
| `reading_score` | Reading score from 0 to 100 |
| `writing_score` | Writing score from 0 to 100 |

## Limitations and responsible use

- The dataset and feature definitions determine what the model can learn; performance may not generalize to other schools or populations.
- Demographic and socioeconomic fields can encode historical bias. Predictions should be reviewed carefully and never used as the sole basis for high-impact decisions.
- The output is an estimated mathematics score, not a diagnosis, official grade, or guarantee of future performance.
- Pickle files should only be loaded from trusted sources.

## Author

**Aryan Pratap Singh**

- GitHub: [@AryanPratap-Singh](https://github.com/AryanPratap-Singh)
- Email: aryansingh87615@gmail.com
