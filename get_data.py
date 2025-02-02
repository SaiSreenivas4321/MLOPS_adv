import os
import sys
import json

from dotenv import load_dotenv

import certifi
import pandas as pd
import numpy as np
import pymongo

#MLOPS_adv\networksecurity\exception\__init__.py

from networksecurity.exception.exception import NetworkSecurityException
#from networksecurity.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


class NetworkDataExtract():
    def __iniit__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def pushing_data_to_mongodb(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    if __name__ =='__main__':
        pass
