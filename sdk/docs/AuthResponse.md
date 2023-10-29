# AuthResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_history_id** | **str** |  | [optional] 
**result_code** | **int** |  | [optional] 
**result_message** | **str** |  | [optional] 
**authorized** | **bool** |  | [optional] 
**auth_details** | [**AuthDetails**](AuthDetails.md) |  | [optional] 

## Example

```python
from autharmor_python.models.auth_response import AuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthResponse from a JSON string
auth_response_instance = AuthResponse.from_json(json)
# print the JSON string representation of the object
print AuthResponse.to_json()

# convert the object into a dict
auth_response_dict = auth_response_instance.to_dict()
# create an instance of AuthResponse from a dict
auth_response_form_dict = auth_response.from_dict(auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


