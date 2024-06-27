import os

'''
    This is the configuration file for the training pipeline.
    This file contains the configuration values that are used in the training pipeline.
    artifact_dir: The directory where the artifacts will be stored
    file_name: The name of the file where the data will be stored
    train_file_name: The name of the file where the training data will be stored
    test_file_name: The name of the file where the testing data will be stored
    preprocessing_object_file_name: The name of the file where the preprocessing object will be stored
    model_file_name: The name of the file where the model will be stored
    schema_file_path: The path to the schema file
    schema_drop_cols: The key in the schema file where the columns to be dropped are stored
    
'''

TARGET_COLUMN = "class"
PIPELINE_NAME = "sensor"
ARTIFACT_DIR = "artifact"
FILE_NAME = "sensor.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"


"""
 data  ingestion realted constant values 
"""

DATA_INGESTION_COLLECTION_NAME: str = "sensor"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2