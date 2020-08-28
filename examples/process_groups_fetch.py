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
    'host': 'HOST-9A4A77A65E91519C',
    'host': 'HOST-6012FE1F9A720968',
    'managementZone': 789692305037011054
}
process_group = dt_client.get_all_process_groups(params=params).json()

with open('process_groups.json', 'w') as f:
    json.dump(obj=process_group, fp=f, indent=4)