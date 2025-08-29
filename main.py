from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig,DataValidationConfig


import sys

if __name__ == '__main__':
    try:
        trainingPipelineConfig=TrainingPipelineConfig()
        dataIngestionConfig=DataIngestionConfig(trainingPipelineConfig)
        data_validation_config=DataValidationConfig(trainingPipelineConfig)
        
        
        
        
        data_ingestion=DataIngestion(dataIngestionConfig)
        logging.info("Initiate the data Ingestion")
        dataIngestionArtifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataIngestionArtifact)

        data_validation=DataValidation(dataIngestionArtifact,data_validation_config)
        logging.info("initaite the data validatoin")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)


    except Exception as e:
        raise NetworkSecurityException(e,sys)