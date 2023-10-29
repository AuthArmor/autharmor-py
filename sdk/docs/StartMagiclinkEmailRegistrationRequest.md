# StartMagiclinkEmailRegistrationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** |  | [optional] 
**timeout_in_seconds** | **int** |  | [optional] 
**registration_redirect_url** | **str** |  | [optional] 
**action_name** | **str** |  | [optional] 
**short_msg** | **str** |  | [optional] 
**context_data** | **Dict[str, str]** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.start_magiclink_email_registration_request import StartMagiclinkEmailRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartMagiclinkEmailRegistrationRequest from a JSON string
start_magiclink_email_registration_request_instance = StartMagiclinkEmailRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print StartMagiclinkEmailRegistrationRequest.to_json()

# convert the object into a dict
start_magiclink_email_registration_request_dict = start_magiclink_email_registration_request_instance.to_dict()
# create an instance of StartMagiclinkEmailRegistrationRequest from a dict
start_magiclink_email_registration_request_form_dict = start_magiclink_email_registration_request.from_dict(start_magiclink_email_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


