# StartChangeMagiclinkEmailRegistrationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout_in_seconds** | **int** |  | [optional] 
**timeout_utc_datetime** | **datetime** |  | [optional] 

## Example

```python
from autharmor_python.models.start_change_magiclink_email_registration_response import StartChangeMagiclinkEmailRegistrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartChangeMagiclinkEmailRegistrationResponse from a JSON string
start_change_magiclink_email_registration_response_instance = StartChangeMagiclinkEmailRegistrationResponse.from_json(json)
# print the JSON string representation of the object
print StartChangeMagiclinkEmailRegistrationResponse.to_json()

# convert the object into a dict
start_change_magiclink_email_registration_response_dict = start_change_magiclink_email_registration_response_instance.to_dict()
# create an instance of StartChangeMagiclinkEmailRegistrationResponse from a dict
start_change_magiclink_email_registration_response_form_dict = start_change_magiclink_email_registration_response.from_dict(start_change_magiclink_email_registration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


