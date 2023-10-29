# ValidateMagiclinkEmailRegistrationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**magiclink_email_registration_type** | [**MagiclinkEmailRegistrationType**](MagiclinkEmailRegistrationType.md) |  | [optional] 
**user_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**context_data** | **Dict[str, str]** |  | [optional] 

## Example

```python
from autharmor_python.models.validate_magiclink_email_registration_response import ValidateMagiclinkEmailRegistrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateMagiclinkEmailRegistrationResponse from a JSON string
validate_magiclink_email_registration_response_instance = ValidateMagiclinkEmailRegistrationResponse.from_json(json)
# print the JSON string representation of the object
print ValidateMagiclinkEmailRegistrationResponse.to_json()

# convert the object into a dict
validate_magiclink_email_registration_response_dict = validate_magiclink_email_registration_response_instance.to_dict()
# create an instance of ValidateMagiclinkEmailRegistrationResponse from a dict
validate_magiclink_email_registration_response_form_dict = validate_magiclink_email_registration_response.from_dict(validate_magiclink_email_registration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


