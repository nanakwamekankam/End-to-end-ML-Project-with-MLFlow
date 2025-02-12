import joblib
import numpy
import pandas as pd
from pathlib import Path
from mlProject import logger

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('End-to-end-ML-Project-with-MLFlow/artifacts/model_trainer'))

    def predict(self, data):
       logger.info("----------------- Prediction Initiated -----------------")
       
       return self.model.predict(data)

