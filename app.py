import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from student_dashboard.component.ingestion import DataIngestion
from student_dashboard.component.data_transformation import data_transformation
from student_dashboard.component.model_trainer import ModelTrainer


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


if __name__ == "__main__":
    main()
