import os
import sys
import numpy as np
import pandas as pd



"""
Definig common constant variable for training pipeline

"""
TARGET_COLUMN = "Result"
PIPELINE_NAME:str = "NetworkSecurity"
ARTIFACT_DIR:str = "Artifacts"
FILE_NAME:str = "NetworkData.csv"


TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("data_schema","schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"

SAVED_MODELS = os.path.join("saved_models")


"""
Data Ingestion related constant startwith Data_Ingestion with Name 

"""
DATA_INGESTION_COLLECTION_NAME:str ="NetworkData"
DATA_INGESTION_DATABASE_NAME:str  = "MLOPS"
DATA_INGESTION_DIR:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str ="feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2


"""
Data Validation related constant start with Data_validation with name 

"""

"""
   Data Validation related constant start with Data_Transformation with name 
"""


"""
   Data Validation related constant start with Model_Trainer with name 
"""

"""
   Data Validation related constant start with Model_Evalaution with name 
"""

"""
   Data Validation related constant start with Model_Pusher with name 
"""