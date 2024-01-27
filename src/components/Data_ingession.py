import os
import sys
from src.Exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngessionCongig:
    train_data_path:str =os.path.join('artifacts','train.csv')
    test_data_path:str =os.path.join('artifacts','test.csv')
    row_data_path:str =os.path.join('artifacts','row.csv')

class DataIngession:
    def __init__(self):
        self.ingession_config = DataIngessionCongig()

    def initiate_data_ingession(self):
        logging.info('entered the Data ingession method or component')

        try:
            df  =pd.read_csv(r'F:\machine learning\end to end projects\Notebook\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingession_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingession_config.row_data_path,index=False,header=True)
            logging.info('train test split initiated')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=43)
            train_set.to_csv(self.ingession_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingession_config.test_data_path,index=False,header=True)
            logging.info("ingesstion of the data is completed")
            return(
                self.ingession_config.train_data_path,
                self.ingession_config.test_data_path,

            )


        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=='__main__':
    obj = DataIngession()
    obj.initiate_data_ingession()