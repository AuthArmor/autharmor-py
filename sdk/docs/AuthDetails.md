# AuthDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_details** | [**RequestDetails**](RequestDetails.md) |  | [optional] 
**response_details** | [**AuthResponseDetails**](AuthResponseDetails.md) |  | [optional] 

## Example

```python
from autharmor_python.models.auth_details import AuthDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AuthDetails from a JSON string
auth_details_instance = AuthDetails.from_json(json)
# print the JSON string representation of the object
print AuthDetails.to_json()

# convert the object into a dict
auth_details_dict = auth_details_instance.to_dict()
# create an instance of AuthDetails from a dict
auth_details_form_dict = auth_details.from_dict(auth_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


