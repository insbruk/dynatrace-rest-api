import os; import sys; sys.path.append(os.path.dirname(os.getcwd()))
import json
from dynatrace.api import Dynatrace


host = 'DYNATRACE_HOST'
token = 'DYNATRACE_TOKEN'

dt_client = Dynatrace(
    host=host,
    token=token,
)

params = {
    'tag': '[AWS]ServiceName:app-name',
    'startTimestamp': 1593993600000,
    'endTimestamp': 1594155600000,
}
hosts = dt_client.get_all_hosts(params=params).json()


with open('hosts.json', 'w') as f:
    json.dump(obj=hosts, fp=f, indent=4)