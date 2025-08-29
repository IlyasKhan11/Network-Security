import os
import sys
import numpy as np
import pandas as pd


"""
Defining common constants variables for traning pipelines
"""

TARGET_COLUMN="Result"
PIPELINE_NAME:str="NetworkSecurity"
ARTIFACT_DIR:str="Artifacts"
FILE_NAME:str="phisingData.csv"

TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"

SCHEMA_FILE_PATH=os.path.join("data_schema","schema.yaml")


"""
Data ingestion related constants
"""

DATA_INGESTION_DATABASE_NAME="NetworkData"
DATA_INGESTION_COLLECTION_NAME="Project"
DATA_INGESTION_DIR_NAME='data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR="feature_store"
DATA_INGESTION_INGESTED_DIR="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION=0.2

"""
Data validation related constants
"""
DATA_VALIDATION_DIR_NAME:str="data_validation"
DATA_VALIDATION_VALID_DIR:str="validation"
DATA_VALIDATION_INVALID_DIR:str="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILENAME:str="report.yaml"

