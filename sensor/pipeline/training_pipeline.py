from sensor.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from sensor.components.data_ingestion import DataIngestion
from sensor.exception import SensorException
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.logger import logging
import sys , os

class TrainPipeline:
    
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
        
    
    def start_data_ingestion(self)->DataIngestionArtifact:
        
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config = self.training_pipeline_config)
            
            logging.info("Starting the data ingestion process")
            
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)
                
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            logging.info("Data ingestion process completed and artifacts are created : {data_ingestion_artifact}")
            return data_ingestion_artifact
                    
        except SensorException as e:
            logging.error(f"Error while exporting data into feature store {e}")
            raise e