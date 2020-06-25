import requests


class Dynatrace:
    # This class provides ability to
    # To pass the request data in JSON format, use header Content-type: application/json.
    # For all requests that return data, the default Accept is application/xml.
    # To request that data be returned in JSON format, use header Accept: application/json.
    def __init__(self, host, token):
        self.host = host
        self.token = token
        self.session = requests.Session()
        self.session.headers.update(
            {
                'Authorization': f'Api-Token {self.token}',
            }
        )

    def get_time(self):
        response = self.session.get(
            url=f'{self.host}/api/v1/time'
        )
        return response

    def get_metric_data(self, entity, params):
        return self.session.get(
            url=f'{self.host}/api/v1/timeseries/{entity}',
            params=params,
        )

    def get_response_times(self):
        pass

    def get_http_4xx_errors(self):
        pass

    def get_http_5xx_errors(self):
        pass

