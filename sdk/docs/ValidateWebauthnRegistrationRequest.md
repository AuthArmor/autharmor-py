# ValidateWebauthnRegistrationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_validation_token** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.validate_webauthn_registration_request import ValidateWebauthnRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateWebauthnRegistrationRequest from a JSON string
validate_webauthn_registration_request_instance = ValidateWebauthnRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print ValidateWebauthnRegistrationRequest.to_json()

# convert the object into a dict
validate_webauthn_registration_request_dict = validate_webauthn_registration_request_instance.to_dict()
# create an instance of ValidateWebauthnRegistrationRequest from a dict
validate_webauthn_registration_request_form_dict = validate_webauthn_registration_request.from_dict(validate_webauthn_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


