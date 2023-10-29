# ValidateWebauthnRegistrationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.validate_webauthn_registration_response import ValidateWebauthnRegistrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateWebauthnRegistrationResponse from a JSON string
validate_webauthn_registration_response_instance = ValidateWebauthnRegistrationResponse.from_json(json)
# print the JSON string representation of the object
print ValidateWebauthnRegistrationResponse.to_json()

# convert the object into a dict
validate_webauthn_registration_response_dict = validate_webauthn_registration_response_instance.to_dict()
# create an instance of ValidateWebauthnRegistrationResponse from a dict
validate_webauthn_registration_response_form_dict = validate_webauthn_registration_response.from_dict(validate_webauthn_registration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


