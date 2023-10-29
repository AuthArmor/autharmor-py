# ValidateAuthResponseDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_history_id** | **str** |  | [optional] 
**result_code** | **int** |  | [optional] 
**result_message** | **str** |  | [optional] 
**authorized** | **bool** |  | [optional] 
**auth_details** | [**AuthDetails**](AuthDetails.md) |  | [optional] 
**context_data** | **Dict[str, str]** |  | [optional] 

## Example

```python
from autharmor_python.models.validate_auth_response_details import ValidateAuthResponseDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAuthResponseDetails from a JSON string
validate_auth_response_details_instance = ValidateAuthResponseDetails.from_json(json)
# print the JSON string representation of the object
print ValidateAuthResponseDetails.to_json()

# convert the object into a dict
validate_auth_response_details_dict = validate_auth_response_details_instance.to_dict()
# create an instance of ValidateAuthResponseDetails from a dict
validate_auth_response_details_form_dict = validate_auth_response_details.from_dict(validate_auth_response_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


