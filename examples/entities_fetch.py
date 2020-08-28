import os; import sys; sys.path.append(os.path.dirname(os.getcwd()))
import json
from dynatrace.api import Dynatrace


host = 'DYNATRACE_HOST'
token = 'DYNATRACE_TOKEN'

dt_client = Dynatrace(
    host=host,
    token=token,
)

entities = dt_client.get_entities_list().json()

with open('entities.json', 'w') as f:
    json.dump(obj=entities, fp=f, indent=4)