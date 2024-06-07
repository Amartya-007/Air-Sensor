from dataclasses import dataclass
import os
import pymongo

@dataclass


class EnvironmentVariable:
    mongo_db_url: str = os.getenv("MONGO_DB_URL")
   


    
env_vars = EnvironmentVariable()
mongo_db_client = pymongo.MongoClient(env_vars.mongo_db_url)