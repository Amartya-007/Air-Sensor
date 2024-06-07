from sensor.exception import SensorException
import sys
from sensor.logger import logging
from sensor.utils import dump_csv_to_mongo

# def test_sensor_error():
#     try:
#         logging.info("channa mere aa mere aa channa mere aa mere aa beliya o piya oo piyaa ")
#         a = 1 / 0  # This line will raise a ZeroDivisionError
#     except Exception as e:
#         raise SensorException(e)

if __name__ == '__main__':
    file_path = r"C:\Users\DELL\Desktop\AirSensor\Air-Sensor\aps_failure_training_set1.csv"
    database_name = "Air_sensor"
    collection_name = "sensor_data"
    dump_csv_to_mongo(file_path, database_name, collection_name)
    
    
    
    
    
    
    # try:
    #     test_sensor_error()
    # except Exception as e:
    #     print(e)
