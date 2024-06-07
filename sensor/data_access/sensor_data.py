import sys
from typing import List,Optional
import numpy as np
import pandas as pd
from sensor.exception import SensorException
import json
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant.database import DATABASE_NAME, COLLECTION_NAME

class SensorData:
    """
    THIS CLASS HELPS TO EXPORT ENTIRE MONOGO DB COLLECTION AS PANDAS DATAFRAME
    """
    def __init__(self):
        
        try:
            self.mongo_client =MongoDBClient(database_name=DATABASE_NAME)
            
        except Exception as e:
            
            