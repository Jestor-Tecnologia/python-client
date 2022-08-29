class JestorApiException(Exception):
    def __init__(self, http_response, *args):
        super().__init__(args)
        self.status_code = http_response.status_code

        try:
            self.message = http_response.json()['data']['message']
        except:
            self.message = http_response.text

    def __str__(self):
        return f'<{self.status_code}> - {self.message}'