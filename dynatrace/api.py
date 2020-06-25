import requests


class Dynatrace:
    # This class provides ability to
    # To pass the request data in JSON format, use header Content-type: application/json.
    # For all requests that return data, the default Accept is application/xml.
    # To request that data be returned in JSON format, use header Accept: application/json.
    def __init__(self, host, token, fiddler=False):
        self.host = host
        self.token = token
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers.update(
            {
                'Authorization': f'Api-Token {self.token}',
                'Content-Type': 'application/json'
            }
        )
        if fiddler:
            self.session.proxies = {
                'http': 'http://127.0.0.1:8888',
                'https': 'http://127.0.0.1:8888',
            }

    def get_time(self):
        return self.session.get(
            url=f'{self.host}/api/v1/time'
        )

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

    def get_dashboard_by_id(self, id):
        # Fetch the configuration of a specific dashboard
        return self.session.get(
            url=f'{self.host}/api/config/v1/dashboards/{id}',
        )

    def get_all_dashboards(self):
        # Fetch the list of all dashboards
        return self.session.get(
            url=f'{self.host}/api/config/v1/dashboards',
        )

    def validate_dashboard(self, data):
        # Validate the configuration of a new dashboard
        return self.session.post(
            url=f'{self.host}/api/config/v1/dashboards/validator',
            data=data,
        )

    def create_dashboard(self, data):
        # Create a new dashboard
        return self.session.post(
            url=f'{self.host}/api/config/v1/dashboards',
            json=data,
        )

    def validate_dashboard_update(self, id, data):
        # Validate the intended configuration update
        return self.session.post(
            url=f'{self.host}/api/config/v1/dashboards/{id}/validator',
            data=data,
        )

    def update_dashboard(self, id, data):
        # Update the configuration of a specific dashboard
        return self.session.put(
            url=f'{self.host}/api/config/v1/dashboards/{id}',
            json=data,
        )

    def delete_dashboard(self, id):
        # Deletes the specified dashboard.
        return self.session.delete(
            url=f'{self.host}/api/config/v1/dashboards/{id}',
        )

    def get_all_processes(self, params=None):
        # Fetches the list of all processes in your Dynatrace environment,
        # along with their parameters and relationships.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/infrastructure/processes',
            params=params,
        )

    def get_process(self, id, params=None):
        # Gets the parameters of the specified process.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/infrastructure/processes/{id}',
            params=params,
        )

    def get_all_process_groups(self, params=None):
        # Fetches the list of all process groups in your Dynatrace environment,
        # along with their parameters and relationships.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/infrastructure/process-groups',
            params=params,
        )

    def get_process_group(self, id, params=None):
        # Gets the parameters of the specified process group.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/infrastructure/process-groups/{id}',
            params=params,
        )

    def get_all_hosts(self, params=None):
        # Gets the list of all hosts in your Dynatrace environment,
        # along with their parameters.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/infrastructure/hosts',
            params=params,
        )

    def get_host(self, id, params=None):
        # Gets the parameters of the specified host.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/infrastructure/hosts/{id}',
            params=params,
        )

    def get_all_metric_definitions(self, source='', detailed_source=''):
        # TODO: add optional parameters to request
        return self.session.get(
            url=f'{self.host}/api/v1/timeseries',
        )

    def get_metric_definition(self, timeseries_id):
        # Gets the definition of the specified metric.
        return self.session.get(
            url=f'{self.host}/api/v1/timeseries/{timeseries_id}',
        )

    def get_metric_datapoints(self, timeseries_id, params):
        # Gets the definition of the specified metric.
        return self.session.get(
            url=f'{self.host}/api/v1/timeseries/{timeseries_id}',
            params=params,
        )
