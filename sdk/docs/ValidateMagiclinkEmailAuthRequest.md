# ValidateMagiclinkEmailAuthRequest


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
from autharmor_python.models.validate_magiclink_email_auth_request import ValidateMagiclinkEmailAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateMagiclinkEmailAuthRequest from a JSON string
validate_magiclink_email_auth_request_instance = ValidateMagiclinkEmailAuthRequest.from_json(json)
# print the JSON string representation of the object
print ValidateMagiclinkEmailAuthRequest.to_json()

# convert the object into a dict
validate_magiclink_email_auth_request_dict = validate_magiclink_email_auth_request_instance.to_dict()
# create an instance of ValidateMagiclinkEmailAuthRequest from a dict
validate_magiclink_email_auth_request_form_dict = validate_magiclink_email_auth_request.from_dict(validate_magiclink_email_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


