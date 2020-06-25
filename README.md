# dynatrace-python-rest-api
Python rest api library for dynatrace saas

# Installation
```
pip install git+https://github.com/insbruk/dynatrace-python-rest-api.git
```

# Examples 
```python
from dynatrace.api import Dynatrace

dt_client = Dynatrace(
    host='<<host>>',
    token='<<token>>'
)
params = {
    'tag': '[AWS]ServiceName:<<service-name>>'
}
hosts = dt_client.get_all_hosts(params=params).json()
print(hosts)
```
Response:
```json
[
    {
        "entityId": "123456",
        "...": "..."
    },
    {
        "entityId": "123456",
        "...": "..."
    }
]
```

# For contributors
I am happy for any PR requests, let's fork and provide your changes.
Please look into contribution guidelines.