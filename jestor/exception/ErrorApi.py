class ErrorApi(Exception):
    def __init__(self, status_code, message, *args):
        super().__init__(args)
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f'<{self.status_code}> - {self.message}'