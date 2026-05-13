import os 
import sys
from  src.exeception import CustomException
from src.logger import  logging  
import  pandas as pd

from sklearn.model_selection  import  train_test_split
from  dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestation_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("entered the ingestation method  or componenet ")
        try:
            df=pd.read_csv(R"E:\Machine_Learning\mlproject-main\notebook\data\stud.csv")
            logging.info("read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestation_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestation_config.raw_data_path,index=False,header=True)

            logging.info("Train test  split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=34)
            train_set.to_csv(self.ingestation_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestation_config.test_data_path,index=False,header=True)

            logging.info("Ingstion of the data is complted")

            return (
                self.ingestation_config.train_data_path,
                self.ingestation_config.test_data_path

            )
        except Exception as e :
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
