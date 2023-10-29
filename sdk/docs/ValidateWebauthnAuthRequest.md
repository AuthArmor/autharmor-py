# ValidateWebauthnAuthRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_validation_token** | **str** |  | [optional] 
**auth_request_id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**nonce** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.validate_webauthn_auth_request import ValidateWebauthnAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateWebauthnAuthRequest from a JSON string
validate_webauthn_auth_request_instance = ValidateWebauthnAuthRequest.from_json(json)
# print the JSON string representation of the object
print ValidateWebauthnAuthRequest.to_json()

# convert the object into a dict
validate_webauthn_auth_request_dict = validate_webauthn_auth_request_instance.to_dict()
# create an instance of ValidateWebauthnAuthRequest from a dict
validate_webauthn_auth_request_form_dict = validate_webauthn_auth_request.from_dict(validate_webauthn_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


