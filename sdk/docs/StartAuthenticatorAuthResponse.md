# StartAuthenticatorAuthResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_validation_token** | **str** |  | [optional] 
**auth_request_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**visual_verify_value** | **str** |  | [optional] 
**response_code** | **int** |  | [optional] 
**response_message** | **str** |  | [optional] 
**qr_code_data** | **str** |  | [optional] 
**push_message_sent** | **bool** |  | [optional] 
**timeout_in_seconds** | **int** |  | [optional] 
**timeout_utc_datetime** | **datetime** |  | [optional] 

## Example

```python
from autharmor_python.models.start_authenticator_auth_response import StartAuthenticatorAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartAuthenticatorAuthResponse from a JSON string
start_authenticator_auth_response_instance = StartAuthenticatorAuthResponse.from_json(json)
# print the JSON string representation of the object
print StartAuthenticatorAuthResponse.to_json()

# convert the object into a dict
start_authenticator_auth_response_dict = start_authenticator_auth_response_instance.to_dict()
# create an instance of StartAuthenticatorAuthResponse from a dict
start_authenticator_auth_response_form_dict = start_authenticator_auth_response.from_dict(start_authenticator_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


