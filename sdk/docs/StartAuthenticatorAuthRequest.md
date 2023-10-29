# StartAuthenticatorAuthRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**nonce** | **str** |  | [optional] 
**send_push** | **bool** |  | [optional] 
**use_visual_verify** | **bool** |  | [optional] 
**timeout_in_seconds** | **int** |  | [optional] 
**origin_location_data** | [**LocationData**](LocationData.md) |  | [optional] 
**action_name** | **str** |  | [optional] 
**short_msg** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.start_authenticator_auth_request import StartAuthenticatorAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartAuthenticatorAuthRequest from a JSON string
start_authenticator_auth_request_instance = StartAuthenticatorAuthRequest.from_json(json)
# print the JSON string representation of the object
print StartAuthenticatorAuthRequest.to_json()

# convert the object into a dict
start_authenticator_auth_request_dict = start_authenticator_auth_request_instance.to_dict()
# create an instance of StartAuthenticatorAuthRequest from a dict
start_authenticator_auth_request_form_dict = start_authenticator_auth_request.from_dict(start_authenticator_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


