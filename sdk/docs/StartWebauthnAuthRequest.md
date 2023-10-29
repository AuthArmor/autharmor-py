# StartWebauthnAuthRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**timeout_in_seconds** | **int** |  | [optional] 
**origin_location_data** | [**LocationData**](LocationData.md) |  | [optional] 
**action_name** | **str** |  | [optional] 
**short_msg** | **str** |  | [optional] 
**webauthn_client_id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**nonce** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.start_webauthn_auth_request import StartWebauthnAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartWebauthnAuthRequest from a JSON string
start_webauthn_auth_request_instance = StartWebauthnAuthRequest.from_json(json)
# print the JSON string representation of the object
print StartWebauthnAuthRequest.to_json()

# convert the object into a dict
start_webauthn_auth_request_dict = start_webauthn_auth_request_instance.to_dict()
# create an instance of StartWebauthnAuthRequest from a dict
start_webauthn_auth_request_form_dict = start_webauthn_auth_request.from_dict(start_webauthn_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


