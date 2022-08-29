class ErrorApi(Exception):
    def __init__(self, status_code, response, *args):
        super().__init__(args)
        self.status_code = status_code

        try:
            self.message = response.json()['data']['message']
        except:
            self.message = response.text

    def __str__(self):
        return f'<{self.status_code}> - {self.message}'