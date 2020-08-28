import os; import sys; sys.path.append(os.path.dirname(os.getcwd()))
import json
from dynatrace.api import Dynatrace


host = 'DYNATRACE_HOST'
token = 'DYNATRACE_TOKEN'

dt_client = Dynatrace(
    host=host,
    token=token,
)

r = dt_client.get_process_group(
    id='PROCESS_GROUP-18CCDF406CAD0912'
)

services = r.json()['toRelationships']['runsOn']

params = {
        'includeData': 'true',
        'aggregationType': 'COUNT',
        'relativeTime': 'month',
        'startTimestamp': 1565309322000,
        'endTimestamp': 1565359722000,
        'queryMode': 'SERIES',
        'entity': services
    }

r = dt_client.get_timeseries_datapoints(
    id='com.dynatrace.builtin:service.requestspermin',
    params=params,
)

print(r.text)