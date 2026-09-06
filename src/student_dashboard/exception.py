import sys

def error_message_detail(error, error_detail):
    _, _, exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno
    return file_name, line_number

class custom_error(Exception):
    def __init__(self, error_message, error_detail=sys):
        super().__init__(error_message)
        file_name, line_number = error_message_detail(
            error_message,
            error_detail
        )
        self.file_name=file_name
        self.line_number=line_number
        self.error_message=error_message
    def __str__(self):
        return (
            f"error in {self.file_name}"
            f"line number: {self.line_number}: "
            f"{self.error_message}"
            )