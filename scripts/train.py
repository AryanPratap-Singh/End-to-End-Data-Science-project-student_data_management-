import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from student_dashboard.component.data_transformation import data_transformation
from student_dashboard.component.ingestion import DataIngestion
from student_dashboard.component.model_trainer import ModelTrainer


def main() -> None:
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()
    transformer = data_transformation()
    train_arr, test_arr, _ = transformer.initiate_data_transformation(
        train_path, test_path
    )
    score = ModelTrainer().initiate_model_trainer(train_arr, test_arr)
    print(f"Model R² score: {score:.4f}")


if __name__ == "__main__":
    main()
