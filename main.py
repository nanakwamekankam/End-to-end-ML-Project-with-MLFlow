from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline

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