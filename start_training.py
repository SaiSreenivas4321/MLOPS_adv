import os
import sys

from networksecurity.exception.exception import NetworkSecurityException


from networksecurity.logger.logger import logging

from networksecurity.pipeline.training_pipeline import Trainingpipeline

def start_training():
    try:
        model_training = Trainingpipeline()
        model_training.run_pipeline()
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    

if __name__ =="__main__":
    start_training()

