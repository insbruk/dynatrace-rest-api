import requests

requests.packages.urllib3.disable_warnings()


class Dynatrace:
    def __init__(self, host, token, fiddler=False):
        # For reference:
        # https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication/
        # https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-response-codes/
        # https://www.dynatrace.com/support/help/dynatrace-api/basics/access-limit/
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

    def get_active_gates(self, params: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/activegates/get-all/
        # Lists all ActiveGates that are currently connected to the environment
        # or have been connected during the last 2 hours.
        return self.session.get(
            url=f'{self.host}/api/v2/activeGates',
            params=params
        )

    def get_active_gate(self, id):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/activegates/get-activegate/
        # Gets the information about the specified ActiveGate.
        return self.session.get(
            url=f'{self.host}/api/v2/activeGates/{id}'
        )

    def get_cluster_time(self):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/cluster-information/
        # The Cluster information API enables you to check the version and internal time of your Dynatrace environment.
        return self.session.get(
            url=f'{self.host}/api/v1/time'
        )

    def get_custom_tags(self, params: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/custom-tags/get-tags/
        # Lists all custom tags assigned to the specified monitored entities.
        # Automatically applied tags and imported tags are not included.
        return self.session.get(
            url=f'{self.host}/api/v2/tags',
            params=params
        )

    def post_custom_tags(self, params: dict = {}, body: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/custom-tags/post-tags/
        # Add custom tags to the specified monitored entities.
        return self.session.post(
            url=f'{self.host}/api/v2/tags',
            params=params,
            data=body
        )

    def delete_custom_tags(self, params: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/custom-tags/del-tags/
        # Deletes the specified custom tag from the specified monitored entities.
        return self.session.delete(
            url=f'{self.host}/api/v2/tags',
            params=params,
        )

    def get_events(self, params: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/events/get-events-feed/
        # Lists all of your environment's events and their parameters
        return self.session.get(
            url=f'{self.host}/api/v1/events',
            params=params,
        )

    def get_event(self, id):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/events/get-event/
        # Lists parameters of the specified event.
        return self.session.get(
            url=f'{self.host}/api/v1/events/{id}',
        )

    def post_event(self, body: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/events/post-event/
        # Pushes custom events from third-party integrations to one or more monitored entities.
        return self.session.post(
            url=f'{self.host}/api/v1/events',
            data=body
        )

    def get_all_processes(self, params: dict = {}):
        # Fetches the list of all processes in your Dynatrace environment,
        # along with their parameters and relationships.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/infrastructure/processes',
            params=params,
        )

    def get_process(self, id, params: dict = {}):
        # Gets the parameters of the specified process.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/infrastructure/processes/{id}',
            params=params,
        )

    def get_all_process_groups(self, params: dict = {}):
        # Fetches the list of all process groups in your Dynatrace environment,
        # along with their parameters and relationships.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/infrastructure/process-groups',
            params=params,
        )

    def get_process_group(self, id, params: dict = {}):
        # Gets the parameters of the specified process group.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/infrastructure/process-groups/{id}',
            params=params,
        )

    def get_entities_list(self, params: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/entity-v2/get-entities-list/
        # Lists entities observed within the specified timeframe along with their properties.
        return self.session.get(
            url=f'{self.host}/api/v2/entities',
            params=params,
        )

    def get_entity(self, id, params: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/entity-v2/get-entity/
        # Gets the full list of properties of the specified entity. The actual list depends on the entity type.
        return self.session.get(
            url=f'{self.host}/api/v2/entities/{id}',
            params=params,
        )

    def get_all_hosts(self, params: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-all/
        # Gets the list of all hosts in your Dynatrace environment, along with their parameters.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/infrastructure/hosts',
            params=params,
        )

    def get_host(self, id, params: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-a-host/
        # Gets the parameters of the specified host.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/infrastructure/hosts/{id}',
            params=params,
        )

    def post_host_tags(self, id, params: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/post-tags/
        # Assigns custom tags to the specified host. You only need to provide a tag value.
        # The CONTEXTLESS context will be assigned automatically.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/infrastructure/hosts/{id}',
            params=params,
        )

    def get_timeseries_list(self, params: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v1/metric-definitions/get-list/
        # Lists all metric definitions, along with parameters of each metric available within your environment.
        return self.session.get(
            url=f'{self.host}/api/v1/timeseries',
            params=params,
        )

    def get_timeseries_definition(self, id, params: dict = {}):
        # Gets the definition of the specified metric.
        return self.session.get(
            url=f'{self.host}/api/v1/timeseries/{id}',
            params=params,
        )

    def get_timeseries_datapoints(self, id, params: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v1/read-data-points/get-data-points/
        # Gets the definition of the specified metric.
        return self.session.get(
            url=f'{self.host}/api/v1/timeseries/{id}',
            params=params,
        )

    def fetch_timeseries_datapoints(self, id, body: dict):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v1/read-data-points/post-data-points/
        # Gets the definition of the specified metric.
        return self.session.post(
            url=f'{self.host}/api/v1/timeseries/{id}',
            json=body,
        )

    def get_services(self, params: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-all/
        # Gets a list of all services in your Dynatrace environment, along with their parameters and relationships.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/services',
            params=params,
        )

    def get_service_meta(self, id):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-a-service/
        # Gets the parameters of a specified service.
        return self.session.get(
            url=f'{self.host}/api/v1/entity/services/{id}',
        )

    def get_metric_list(self, params: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/get-all-metrics/
        # Lists all available metrics.
        return self.session.get(
            url=f'{self.host}/api/v2/metrics',
            params=params,
        )

    def get_metric_definition(self, id):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/get-descriptor/
        # Gets the parameters of the specified metric.
        return self.session.get(
            url=f'{self.host}/api/v2/metrics/{id}',
            # params=params,
        )

    def get_metric_datapoints(self, params: dict = {}):
        # https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/get-data-points/
        # Gets data points of the specified metrics.
        return self.session.get(
            url=f'{self.host}/api/v2/metrics/query',
            params=params,
        )

    # Configuration API
    # Dynatrace configuration API helps you keep track of your Dynatrace monitoring environment configurations.
    # https://www.dynatrace.com/support/help/dynatrace-api/configuration-api/

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
