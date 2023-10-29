# StartAutharmorAuthenticatorRegistrationNewUserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**registration_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**date_expires** | **datetime** |  | [optional] 
**auth_method** | **str** |  | [optional] 
**qr_code_data** | **str** |  | [optional] 
**registration_validation_token** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.start_autharmor_authenticator_registration_new_user_response import StartAutharmorAuthenticatorRegistrationNewUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartAutharmorAuthenticatorRegistrationNewUserResponse from a JSON string
start_autharmor_authenticator_registration_new_user_response_instance = StartAutharmorAuthenticatorRegistrationNewUserResponse.from_json(json)
# print the JSON string representation of the object
print StartAutharmorAuthenticatorRegistrationNewUserResponse.to_json()

# convert the object into a dict
start_autharmor_authenticator_registration_new_user_response_dict = start_autharmor_authenticator_registration_new_user_response_instance.to_dict()
# create an instance of StartAutharmorAuthenticatorRegistrationNewUserResponse from a dict
start_autharmor_authenticator_registration_new_user_response_form_dict = start_autharmor_authenticator_registration_new_user_response.from_dict(start_autharmor_authenticator_registration_new_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


