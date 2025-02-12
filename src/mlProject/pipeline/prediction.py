import joblib
from pathlib import Path
from mlProject import logger

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))

    def predict(self, data):
       logger.info("----------------- Prediction Initiated -----------------")
       
       return self.model.predict(data)

