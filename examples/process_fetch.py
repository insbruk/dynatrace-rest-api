import os; import sys; sys.path.append(os.path.dirname(os.getcwd()))
import json
from dynatrace.api import Dynatrace


host = 'DYNATRACE_HOST'
token = 'DYNATRACE_TOKEN'

dt_client = Dynatrace(
    host=host,
    token=token,
)

service = 'app-name'
params = {
    'hostTag': f'[Environment]ServiceName:{service}',
    # 'tag': '[Environment]ServiceName:wpng-search',
    # 'host': 'HOST-929B55F13803AD6A'
}
processes = dt_client.get_all_processes(params=params).json()
processes = [p for p in processes if service in p['discoveredName']]
with open(f'processes_{service}.json', 'w') as f:
    json.dump(obj=processes, fp=f, indent=4)