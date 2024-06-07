import os
import sys
from pandas import DataFrame
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.entity.config_entity import DataIngestionConfig
from sensor.data_access.sensor_data import SensorData
from sklearn.model_selection import train_test_split

class DataIngestion:
    
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            
        except Exception as e:
            raise SensorException(e,sys)
        
    def export_data_into_feature_store(self)->DataFrame:
        
        """
        Export MongoDB collection record as dataframe into feature store
        """
        try:
            logging.info("Exporting data into feature store")
            sensor_data = SensorData()
            
            Dataframe = sensor_data.export_collection_as_dataframe(collection_name = self.data_ingestion_config.collection_name)

            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            
            # creating the folder if it does not exist
            
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            Dataframe.to_csv(feature_store_file_path, index=False,header=True)
            return Dataframe
        
        except Exception as e:
            raise SensorException(e,sys)
        
        
    def split_data_as_train_test(self,dataframe:DataFrame)->None:
        
        """
        Split the data into train and test
        """
        try:
            logging.info("Splitting the data into train and test")
            
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            
            logging.info(f"performed the train test split and the train set shape is {train_set.shape} and test set shape is {test_set.shape}")
            
            logging.info(f"Exiting the split_data_as_train_test method of the Data_Ingestion class")
            
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            logging.info(f"Exporting the train set into the file {self.data_ingestion_config.training_file_path}")
            
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False,header=True)
            
            logging.info(f"Succesfully Exported the train set into the file")
            
        
        except Exception as e:
            raise SensorException(e,sys)
            
            
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        
        try:
            dataframe = self.export_data_into_feature_store()
            
            self.split_data_as_train_test(dataframe=dataframe)
            
            data_ingestion_artifact = DataIngestionArtifact(training_file_path = self.data_ingestion_config.training_file_path,
                                                            testing_file_path = self.data_ingestion_config.testing_file_path)
            
            return data_ingestion_artifact
        
        except Exception as e:
            raise SensorException(e,sys)
