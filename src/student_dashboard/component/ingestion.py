import os
import sys
from dataclasses import dataclass
from pathlib import Path

SRC_PATH = Path(__file__).resolve().parents[2]
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

import pandas as pd
from sklearn.model_selection import train_test_split

from student_dashboard.component.data_transformation import data_transformation
from student_dashboard.component.model_trainer import ModelTrainer
from student_dashboard.exception import custom_error
from student_dashboard.logger import logging

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the dataset as dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("train test split")
            train_split, test_split= train_test_split(df,test_size=0.2,random_state=42)
            
            train_split.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_split.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("ingestion of data complete")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            raise custom_error(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    
    datatransformation= data_transformation()
    train_arr,test_arr,_=datatransformation.initiate_data_transformation(train_data,test_data)
    
    ModelTrainer= ModelTrainer()
    print(ModelTrainer.initiate_model_trainer(train_arr,test_arr))