import sys
import os
import traceback

def error_message_details(error):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    filename = os.path.basename(exc_tb.tb_frame.f_code.co_filename)
    error_message = f"Error in File : [{filename}] at line [{exc_tb.tb_lineno}] : error is : [{str(error)}]"
    
    return error_message



class SensorException(Exception):
    
    def __init__(self, error):
        super().__init__(str(error))
        self.error_message = error_message_details(error)
    
    
    def __str__(self):
        return self.error_message

