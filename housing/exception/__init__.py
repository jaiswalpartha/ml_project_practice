import os
import sys 


class HousingException(Exception):
    def __init__(self, error_message:Exception):
        super().__init__(error_message)
        self.error_message = HousingException.get_error_details(error_message)
        

    @staticmethod
    def get_error_details(error_message:Exception)->str:
        _,_,exec_tb= sys.exc_info()
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        detailed_error_message = f"Error Occured IN Script:[{file_name}] | Line Number:[{line_number}] | Error Message: [{error_message}]"
        return detailed_error_message

    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return HousingException.__name__().str

        