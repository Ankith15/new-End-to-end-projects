import sys
from dataclasses import dataclass
import numpy as numpy
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.Exception import CustomException
from src.logger import logging
import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path =os.path.join('artifacts',"processor.pkl")

class DataTrasformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        """This is responsible for data transformation"""

        try:
            numerical_score=['writing_score','reading_score']
            categorical_columns=[
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course'
            ]
            num_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median'))
                    ('scaler',StandardScaler())
                ]
                
            )
            cat_pipeline=Pipeline(
                stepps =[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder',OneHotEncoder()),
                    ("scaler",StandardScaler())
                ]
            )
            logging.info('Categorical columns encoding completed')
            logging.info('numerical columns standard scale completed')
            
            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline',num_pipeline,numerical_score),
                    ('categorical_pipe',cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data is done")
            logging.info("obtaining preprocessing object")
            preprocessing_obj= self.get_data_transformer_object()
            target_column_name = "math_score"
            numerical_score =['writing_score',"reading_score"]

            
        except:
            pass