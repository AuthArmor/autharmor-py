# StartAutharmorAutenticatorRegistrationNewUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**timeout_in_seconds** | **int** |  | [optional] 

## Example

```python
from autharmor_python.models.start_autharmor_autenticator_registration_new_user_request import StartAutharmorAutenticatorRegistrationNewUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartAutharmorAutenticatorRegistrationNewUserRequest from a JSON string
start_autharmor_autenticator_registration_new_user_request_instance = StartAutharmorAutenticatorRegistrationNewUserRequest.from_json(json)
# print the JSON string representation of the object
print StartAutharmorAutenticatorRegistrationNewUserRequest.to_json()

# convert the object into a dict
start_autharmor_autenticator_registration_new_user_request_dict = start_autharmor_autenticator_registration_new_user_request_instance.to_dict()
# create an instance of StartAutharmorAutenticatorRegistrationNewUserRequest from a dict
start_autharmor_autenticator_registration_new_user_request_form_dict = start_autharmor_autenticator_registration_new_user_request.from_dict(start_autharmor_autenticator_registration_new_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


