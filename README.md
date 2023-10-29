# Auth Armor Python SDK
Auth Armor provides a SaaS solution to authenticate your users exclusively using passwordless authentication methods such as WebAuthn, magic links and the proprietary Auth Armor mobile app.

This package provides a flexible and full-featured integration with your Python project/product. Its a [openapi generated python sdk](https://github.com/OpenAPITools/openapi-generator). 

## Installation 
```python
pip install autharmor_python
```

## Usage
autharmor_python the autharmor api spec for its operations, in turn you can perform all the operations listed [here](https://docs.autharmor.com/reference) with it.

```python
import autharmor_python
import time
import autharmor_python
from autharmor_python.rest import ApiException
from pprint import pprint
import requests

# 1. Authentication Details - https://docs.autharmor.com/docs/api-overview
client_id = os.environ["client_id"]
client_secret = os.environ["client_secret"]

# 2. Access token
def get_access_token(client_id, client_secret):
    try:
        login_url = f"https://login.autharmor.com/connect/token"
        response = requests.post(
            login_url,
            data={"grant_type": "client_credentials"},
            auth=(client_id, client_secret),
        )

        print(response.status_code)
        if response.status_code == 200:
            return response.json()["access_token"]
        else:
            return None
    except Exception as e:
        pprint(e)
access_token = get_access_token(client_id=client_id, client_secret=client_secret)

# 3. Configuration & Client
configuration = autharmor_python.Configuration(access_token=access_token)
client = autharmor_python.ApiClient(configuration) 

# 4. Call API methods using client instance
try:
    response = autharmor_python.UsersApi(client).v4_users_get()
    data = response.user_records
    pprint(data)
except ApiException as e:
    pprint(e.reason)
    pprint(e.headers)

```


## OpenAPI Specific
- OpenAPI spec file https://api.autharmor.com/swagger/v4/swagger.json
- OpenAPI sdk generated folder - [/sdk](/output)
