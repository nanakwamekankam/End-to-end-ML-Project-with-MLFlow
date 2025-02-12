from flask import Flask, render_template, request
import os
import pandas as pd
import numpy as np
from mlProject.pipeline.prediction import PredictionPipeline


# Initialize Flask
app = Flask(__name__)

@app.route('/', methods=["GET"]) # Route to render homepage
def homepage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
