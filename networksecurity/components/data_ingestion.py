import os
import sys
from typing import List
import numpy as np
import pandas as pd
import pymongo
from sklearn.model_selection import train_test_split


from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


from dotenv import load_dotenv
load_dotenv()

MONGODB_URL=os.getenv("MONGODB_URL")

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def export_collection_as_dataframe(self):
        """
        read data from mongodb
        """
        try:
            database_name=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name

            self.mongo_client=pymongo.MongoClient(MONGODB_URL)

            collection = self.mongo_client[database_name][collection_name]
            df=pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.to_list():
                df=df.drop(columns=["_id"])
            
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def export_data_into_feature_store(self,dataframe):
        """
        stores raw data at filepath defined
        """
        try:
            filepath=self.data_ingestion_config.feature_store_file_path
            location=os.path.dirname(filepath)
            os.makedirs(location,exist_ok=True)
            dataframe.to_csv(filepath,index=False,header=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(s,sys)
        
    def split_dataframe_train_test(self,dataframe):
        try:            
            train_set,test_set=train_test_split(
                dataframe,test_size=self.data_ingestion_config.train_test_split_ratio
            )
            logging.info("Performed train test split on the dataframe")

            logging.info(
                "Exited split_data_as_train_test method of Data_Ingestion class"
            )
            

            filepath_train_test=self.data_ingestion_config.testing_file_path
            dir_path=os.path.dirname(filepath_train_test)

            os.makedirs(dir_path)
            logging.info(f"Exporting train and test file path.")


            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)

            logging.info(f"Exported train and test file path.")

        except Exception as e:
            raise NetworkSecurityException(e,sys)


    def initiate_data_ingestion(self):
        try:
            dataframe=self.export_collection_as_dataframe()
            dataframe=self.export_data_into_feature_store(dataframe)
            self.split_dataframe_train_test(dataframe)
            dataingestionartifact=DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                                        test_file_path=self.data_ingestion_config.testing_file_path)
            return dataingestionartifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)



