## What is the use of sys, so basically any exception that get generated, the sys will have them
import sys
import logging
def error_message_detail(error, error_detail: sys):
    ## Basically gives three infos, but first two aren't imp
    ## exc_tb will hold the main info, like which line, which file, what kind of exception did occur 
    ## tb is nothing but traceback
    _,_,exc_tb=error_detail.exc_info() ## --> exc_info = execution info
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occurd in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno,str(error)

    )
    return error_message

                      ## The Exception is the python's default, basic error class 
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        ## through super I am calling, the default class first, so it makes the initial default things before running custom exception handling
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
