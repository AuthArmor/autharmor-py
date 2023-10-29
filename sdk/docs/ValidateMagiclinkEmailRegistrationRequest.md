# ValidateMagiclinkEmailRegistrationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_validation_token** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.validate_magiclink_email_registration_request import ValidateMagiclinkEmailRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateMagiclinkEmailRegistrationRequest from a JSON string
validate_magiclink_email_registration_request_instance = ValidateMagiclinkEmailRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print ValidateMagiclinkEmailRegistrationRequest.to_json()

# convert the object into a dict
validate_magiclink_email_registration_request_dict = validate_magiclink_email_registration_request_instance.to_dict()
# create an instance of ValidateMagiclinkEmailRegistrationRequest from a dict
validate_magiclink_email_registration_request_form_dict = validate_magiclink_email_registration_request.from_dict(validate_magiclink_email_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


