# AuthProfileDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.auth_profile_details import AuthProfileDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AuthProfileDetails from a JSON string
auth_profile_details_instance = AuthProfileDetails.from_json(json)
# print the JSON string representation of the object
print AuthProfileDetails.to_json()

# convert the object into a dict
auth_profile_details_dict = auth_profile_details_instance.to_dict()
# create an instance of AuthProfileDetails from a dict
auth_profile_details_form_dict = auth_profile_details.from_dict(auth_profile_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


