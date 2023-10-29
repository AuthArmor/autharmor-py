# FinishWebauthnAuthResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_validation_token** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**auth_request_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.finish_webauthn_auth_response import FinishWebauthnAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FinishWebauthnAuthResponse from a JSON string
finish_webauthn_auth_response_instance = FinishWebauthnAuthResponse.from_json(json)
# print the JSON string representation of the object
print FinishWebauthnAuthResponse.to_json()

# convert the object into a dict
finish_webauthn_auth_response_dict = finish_webauthn_auth_response_instance.to_dict()
# create an instance of FinishWebauthnAuthResponse from a dict
finish_webauthn_auth_response_form_dict = finish_webauthn_auth_response.from_dict(finish_webauthn_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


