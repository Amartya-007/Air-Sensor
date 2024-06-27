from dotenv import load_dotenv
import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
from sensor.constant.env_variable import MONGODB_URL_KEY
import os
import logging
load_dotenv()
ca = certifi.where()



class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                logging.info(f"Retrieved MongoDB URL: {mongo_db_url}")

                # Add a print statement to verify the value of mongo_db_url
                print(f"mongo_db_url: {mongo_db_url}")

                if not mongo_db_url:
                    raise ValueError("MONGO_DB_URL environment variable is not set.")

                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name

        except Exception as e:
            logging.error(f"Error initializing MongoDB client: {e}")
            raise

# Test the MongoDB client initialization
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        db_client = MongoDBClient()
        logging.info(f"Connected to database: {db_client.database_name}")
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {e}")
