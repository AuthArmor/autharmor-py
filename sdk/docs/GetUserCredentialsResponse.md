# GetUserCredentialsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_records** | [**List[Credential]**](Credential.md) |  | [optional] 
**page_info** | [**UsersCredentialsResponsePageInfo**](UsersCredentialsResponsePageInfo.md) |  | [optional] 

## Example

```python
from autharmor_python.models.get_user_credentials_response import GetUserCredentialsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserCredentialsResponse from a JSON string
get_user_credentials_response_instance = GetUserCredentialsResponse.from_json(json)
# print the JSON string representation of the object
print GetUserCredentialsResponse.to_json()

# convert the object into a dict
get_user_credentials_response_dict = get_user_credentials_response_instance.to_dict()
# create an instance of GetUserCredentialsResponse from a dict
get_user_credentials_response_form_dict = get_user_credentials_response.from_dict(get_user_credentials_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


