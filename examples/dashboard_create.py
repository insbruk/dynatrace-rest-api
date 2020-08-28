import os; import sys; sys.path.append(os.path.dirname(os.getcwd()))
import json
from dynatrace.api import Dynatrace


host = 'DYNATRACE_HOST'
token = 'DYNATRACE_TOKEN'

dt_client = Dynatrace(
    host=host,
    token=token,
    fiddler=False
)

with open('app-dashboard.json', 'r') as f:
    d = json.load(f)
    r = dt_client.create_dashboard(data=d)
    print(r.text)
