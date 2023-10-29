# GetAuthRequestResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_request_status_id** | **int** |  | [optional] 
**auth_request_status_name** | **str** |  | [optional] 
**auth_response** | [**AuthResponse**](AuthResponse.md) |  | [optional] 

## Example

```python
from autharmor_python.models.get_auth_request_response import GetAuthRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthRequestResponse from a JSON string
get_auth_request_response_instance = GetAuthRequestResponse.from_json(json)
# print the JSON string representation of the object
print GetAuthRequestResponse.to_json()

# convert the object into a dict
get_auth_request_response_dict = get_auth_request_response_instance.to_dict()
# create an instance of GetAuthRequestResponse from a dict
get_auth_request_response_form_dict = get_auth_request_response.from_dict(get_auth_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


