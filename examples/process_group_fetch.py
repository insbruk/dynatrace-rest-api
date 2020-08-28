import os; import sys; sys.path.append(os.path.dirname(os.getcwd()))
import json
from dynatrace.api import Dynatrace


host = 'DYNATRACE_HOST'
token = 'DYNATRACE_TOKEN'

dt_client = Dynatrace(
    host=host,
    token=token,
)

process_group = dt_client.get_process_group(id='PROCESS_GROUP-D7C72AF0AD091488').json()

with open('process_group.json', 'w') as f:
    json.dump(obj=process_group, fp=f, indent=4)