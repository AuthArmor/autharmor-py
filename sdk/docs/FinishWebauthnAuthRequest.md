# FinishWebauthnAuthRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_response_data** | **str** |  | [optional] 
**aa_sig** | **str** |  | [optional] 
**auth_request_id** | **str** |  | [optional] 
**webauthn_client_id** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.finish_webauthn_auth_request import FinishWebauthnAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FinishWebauthnAuthRequest from a JSON string
finish_webauthn_auth_request_instance = FinishWebauthnAuthRequest.from_json(json)
# print the JSON string representation of the object
print FinishWebauthnAuthRequest.to_json()

# convert the object into a dict
finish_webauthn_auth_request_dict = finish_webauthn_auth_request_instance.to_dict()
# create an instance of FinishWebauthnAuthRequest from a dict
finish_webauthn_auth_request_form_dict = finish_webauthn_auth_request.from_dict(finish_webauthn_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


