# StartMagiclinkEmailRegistrationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout_in_seconds** | **int** |  | [optional] 
**timeout_utc_datetime** | **datetime** |  | [optional] 

## Example

```python
from autharmor_python.models.start_magiclink_email_registration_response import StartMagiclinkEmailRegistrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartMagiclinkEmailRegistrationResponse from a JSON string
start_magiclink_email_registration_response_instance = StartMagiclinkEmailRegistrationResponse.from_json(json)
# print the JSON string representation of the object
print StartMagiclinkEmailRegistrationResponse.to_json()

# convert the object into a dict
start_magiclink_email_registration_response_dict = start_magiclink_email_registration_response_instance.to_dict()
# create an instance of StartMagiclinkEmailRegistrationResponse from a dict
start_magiclink_email_registration_response_form_dict = start_magiclink_email_registration_response.from_dict(start_magiclink_email_registration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


