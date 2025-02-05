from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline

# logger.info("Welcome to the custom logging")

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx=================================x")
except Exception as e:
    logger.exception(e)
    raise e

# --------------------------------------------------------------------------------------------------
STAGE_NAME = "Data Validation"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx=================================x")
except Exception as e:
    logger.exception(e)
    raise e

# --------------------------------------------------------------------------------------------------
STAGE_NAME = "Data Transformation"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx=================================x")
except Exception as e:
    logger.exception(e)
    raise e

# --------------------------------------------------------------------------------------------------


