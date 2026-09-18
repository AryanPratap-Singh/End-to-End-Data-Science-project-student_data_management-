import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from student_dashboard.component.ingestion import DataIngestion
from student_dashboard.component.data_transformation import data_transformation
from student_dashboard.component.model_trainer import ModelTrainer

from flask import Flask, request, render_template
from student_dashboard.pipeline.predict_pipeline import CustomData,PredictPipeline
def main():
    ingestion = DataIngestion()
    train_data_path, test_data_path = ingestion.initiate_data_ingestion()

    transformer = data_transformation()
    train_arr, test_arr, _ = transformer.initiate_data_transformation(
        train_data_path,
        test_data_path,
    )

    model_trainer = ModelTrainer()
    score = model_trainer.initiate_model_trainer(train_arr, test_arr)
    print(f"Model R^2 score: {score}")



application=Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "GET":
        return render_template('Home.html')

    data = CustomData(
        gender=request.form.get('gender'),
        race_ethnicity=request.form.get('ethnicity'),
        parental_level_of_education=request.form.get('parental_level_of_education'),
        lunch=request.form.get('lunch'),
        test_preparation_course=request.form.get('test_preparation_course'),
        reading_score=float(request.form.get('reading_score')),
        writing_score=float(request.form.get('writing_score'))
    )
    pred_df = data.get_data_as_data_frame()
    results = PredictPipeline().predict(pred_df)
    return render_template('Home.html', results=results[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0")