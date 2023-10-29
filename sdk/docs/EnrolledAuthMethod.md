# EnrolledAuthMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method_name** | **str** |  | [optional] 
**auth_method_id** | **int** |  | [optional] 
**auth_method_masked_info** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.enrolled_auth_method import EnrolledAuthMethod

# TODO update the JSON string below
json = "{}"
# create an instance of EnrolledAuthMethod from a JSON string
enrolled_auth_method_instance = EnrolledAuthMethod.from_json(json)
# print the JSON string representation of the object
print EnrolledAuthMethod.to_json()

# convert the object into a dict
enrolled_auth_method_dict = enrolled_auth_method_instance.to_dict()
# create an instance of EnrolledAuthMethod from a dict
enrolled_auth_method_form_dict = enrolled_auth_method.from_dict(enrolled_auth_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


