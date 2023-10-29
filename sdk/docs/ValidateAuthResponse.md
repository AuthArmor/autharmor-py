# ValidateAuthResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_request_status_id** | **int** |  | [optional] 
**auth_request_status_name** | **str** |  | [optional] 
**validate_auth_response_details** | [**ValidateAuthResponseDetails**](ValidateAuthResponseDetails.md) |  | [optional] 

## Example

```python
from autharmor_python.models.validate_auth_response import ValidateAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAuthResponse from a JSON string
validate_auth_response_instance = ValidateAuthResponse.from_json(json)
# print the JSON string representation of the object
print ValidateAuthResponse.to_json()

# convert the object into a dict
validate_auth_response_dict = validate_auth_response_instance.to_dict()
# create an instance of ValidateAuthResponse from a dict
validate_auth_response_form_dict = validate_auth_response.from_dict(validate_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


