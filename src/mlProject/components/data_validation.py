import pandas as pd
from mlProject.entity.config_entity import (DataValidationConfig)


class DataValidation:
    def __init__(self, config):
        self.config = config

    def validate_all_columns(self):
        # checks schema to make sure all columns present in the dataset are accounted for
        try:
            validation_status = True
            df = pd.read_csv(self.config.unzip_data_dir)
            columns = list(df.columns)
            schema = self.config.all_schema

            for column in columns:
                if column not in schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status} (Unexpected column{column} found in dataset not in schema)")

            # Check for datatype mismatches
            for column, expected_dtype in schema.items():
                if column in df.columns:
                    actual_dtype = df[column].dtype.name  # Get the data type name
                    if actual_dtype != expected_dtype:
                        validation_status = False
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation failed: Column '{column}' expected '{expected_dtype}' but found '{actual_dtype}'.\n")
                        return validation_status  # Exit early if invalid
                else:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation failed: Missing column '{column}'.\n")
                    return validation_status
            
            # If all checks pass
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}\n")

            return validation_status
        
        except Exception as e:
            raise e
    
