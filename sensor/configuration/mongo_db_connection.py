from dotenv import load_dotenv
import os
import pymongo
import logging
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
import certifi 
ca = certifi.where()

load_dotenv()

class MongoDBClient:
    client = None
    
    
    def __init__(self,database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                logging.info(f"retrieved the mongo db url from the environment variable {mongo_db_url}")
                
                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)  #TLS/SSL connection
        
            self.client = MongoDBClient.client
            self.db = self.client[database_name]
            self.database_name = database_name
            
        except Exception as e:
            logging.error(f"Error while connecting to the database {e}")
            raise 
