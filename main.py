from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig,DataValidationConfig,DataTransformationConfig


import sys

if __name__ == '__main__':
    try:
        trainingPipelineConfig=TrainingPipelineConfig()
        dataIngestionConfig=DataIngestionConfig(trainingPipelineConfig)
        data_validation_config=DataValidationConfig(trainingPipelineConfig)
        data_transformation_config=DataTransformationConfig(trainingPipelineConfig)
        
        
        
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


        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        logging.info("Data Transformation started")
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data Transformation completed")

    except Exception as e:
        raise NetworkSecurityException(e,sys)