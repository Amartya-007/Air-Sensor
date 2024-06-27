from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os , sys
from sensor.logger import logging
from  sensor.utils import dump_csv_file_to_mongodb_collection
from sensor.entity.config_entity  import TrainingPipelineConfig,DataIngestionConfig

from sensor.pipeline.training_pipeline import TrainPipeline


if __name__ == '__main__':
    file_path = r"C:\Users\DELL\Desktop\AirSensor\Air-Sensor\aps_failure_training_set1.csv"
    database_name = "AirSensor"
    collection_name = "SensorData"
    dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)
    
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
    
    
