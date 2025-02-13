from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


#configuaration of all components and artifacts genration

from networksecurity.entity.config_entity import DataIngestionEntity
from networksecurity.entity.artifact_entity import DataIngetionArtifact
import os
import sys
import pandas as pd
import numpy as np
import pymongo
from typing import List

from dotenv import load_dotenv
load_dotenv
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


class DataIngestion:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def export_collection_as_DataFrame(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def export_data_into_feature_store(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def split_data_as_train_test(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)      

