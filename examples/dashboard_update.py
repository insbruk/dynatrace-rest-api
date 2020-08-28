import os; import sys; sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))
import json
from dynatrace.api import Dynatrace


host = 'DYNATRACE_HOST'
token = 'DYNATRACE_TOKEN'

dt_client = Dynatrace(
    host=host,
    token=token,
    fiddler=False
)

dashboard_id = '<dashboard_id>'
dashboard_file = f'app-dashboard.json'
r = dt_client.get_dashboard_by_id(id=dashboard_id)
print(r.status_code, r.text)
dashboard_json = r.json()
with open(dashboard_file, 'w') as f:  # for updating local dashboard json
    json.dump(dashboard_json, f, indent=4, sort_keys=True)
with open(dashboard_file, 'r') as f:  # for updating remote dashboard json
    dashboard_json = json.load(f)
    r = dt_client.update_dashboard(id=dashboard_id, data=dashboard_json)
    print(r.status_code, r.text)
