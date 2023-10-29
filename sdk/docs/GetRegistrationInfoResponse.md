# GetRegistrationInfoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_status_name** | **str** |  | [optional] 
**registration_status_code** | **int** |  | [optional] 
**auth_method** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.get_registration_info_response import GetRegistrationInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRegistrationInfoResponse from a JSON string
get_registration_info_response_instance = GetRegistrationInfoResponse.from_json(json)
# print the JSON string representation of the object
print GetRegistrationInfoResponse.to_json()

# convert the object into a dict
get_registration_info_response_dict = get_registration_info_response_instance.to_dict()
# create an instance of GetRegistrationInfoResponse from a dict
get_registration_info_response_form_dict = get_registration_info_response.from_dict(get_registration_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


