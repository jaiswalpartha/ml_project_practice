import os

class HousingException(Exception):
    def __init__(self, error_message: Exception):
        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_error(error_message=error_message)
    
    @staticmethod
    def get_detailed_error(error_message:Exception)->str:
        import sys
        _, _, traceback = sys.exc_info()
        line_no = traceback.tb_frame.f_lineno
        file_name = traceback.tb_frame.f_code.co_filename
        detail_error_massage = f"ERROR OCCURED IN SCRIPT:[{file_name}]||LINE NUM:[{line_no}]||ERROR INFO:[{error_message}]"
        return detail_error_massage
        
    def __str__(self):
        return self.error_message
    def __repr__(self) -> str:
        return HousingException.__name__.str()