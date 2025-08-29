import sys

from networksecurity.logging.logger import logging


class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_detail:sys):
        self.error_message=error_message
        _,_,exec_tb=error_detail.exc_info()

        self.lineno=exec_tb.tb_lineno
        self.filename=exec_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in script: {self.filename} at line: {self.lineno} with message: {self.error_message}"


# if __name__ == "__main__":
#     try:
#         logging.info("Enter the try block.")
#         a=1/0
#         print("this should not run")

#     except Exception as e:
#         raise NetworkSecurityException(e, sys)