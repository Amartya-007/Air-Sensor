from sensor.exception import SensorException
import sys
from sensor.logger import logging

def test_sensor_error():
    try:
        logging.info("channa mere aa mere aa channa mere aa mere aa beliya o piya oo piyaa ")
        a = 1 / 0  # This line will raise a ZeroDivisionError
    except Exception as e:
        raise SensorException(e)

if __name__ == '__main__':
    try:
        test_sensor_error()
    except Exception as e:
        print(e)
