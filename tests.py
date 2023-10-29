client_id = os.environ["client_id"]
client_secret = os.environ["client_secret"]

import time
import autharmor_python
from autharmor_python.rest import ApiException
from pprint import pprint
import requests

# 1. Access token
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

# 2. Configuration & Client
configuration = autharmor_python.Configuration(access_token=access_token)
client = autharmor_python.ApiClient(configuration) 

try:
    response = autharmor_python.UsersApi(client).v4_users_get()
    data = response.user_records
    pprint(data)
except ApiException as e:
    pprint(e.reason)
    pprint(e.headers)