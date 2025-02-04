from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import DataIngestionConfig, DataValidationConfig

class ConfigurationManager:
    def __init__(self):
        self,
        # config_filepath = CONFIG_FILE_PATH
        # param_filepath = PARAMS_FILE_PATH
        # schema_filepath = SCHEMA_FILE_PATH

        self.config = read_yaml(CONFIG_FILE_PATH)
        self.param = read_yaml(PARAMS_FILE_PATH)
        self.schema = read_yaml(SCHEMA_FILE_PATH)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self):
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig( 
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_config
    

    def get_data_validation_config(self):
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            unzip_data_dir= config.unzip_data_dir,
            STATUS_FILE= config.STATUS_FILE,
            all_schema= schema
        )

        return data_validation_config