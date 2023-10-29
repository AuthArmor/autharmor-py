# StartMagiclinkEmailAuthResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_request_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**timeout_in_seconds** | **int** |  | [optional] 
**timeout_utc_datetime** | **datetime** |  | [optional] 

## Example

```python
from autharmor_python.models.start_magiclink_email_auth_response import StartMagiclinkEmailAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartMagiclinkEmailAuthResponse from a JSON string
start_magiclink_email_auth_response_instance = StartMagiclinkEmailAuthResponse.from_json(json)
# print the JSON string representation of the object
print StartMagiclinkEmailAuthResponse.to_json()

# convert the object into a dict
start_magiclink_email_auth_response_dict = start_magiclink_email_auth_response_instance.to_dict()
# create an instance of StartMagiclinkEmailAuthResponse from a dict
start_magiclink_email_auth_response_form_dict = start_magiclink_email_auth_response.from_dict(start_magiclink_email_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


