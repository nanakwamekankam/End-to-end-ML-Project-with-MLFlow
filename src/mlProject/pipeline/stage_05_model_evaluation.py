from mlProject.config.configuration import ConfigurationManager
from mlProject.components.mode_evaluation import ModelEvaluation
from mlProject import logger


STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluator_config = config.get_model_evaluation_config()
        model_evaluator = ModelEvaluation(config=model_evaluator_config)
        model_evaluator.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx=================================x")
    except Exception as e:
        logger.exception(e)
        raise e
