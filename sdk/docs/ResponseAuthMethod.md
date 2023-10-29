# ResponseAuthMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**AuthMethods**](AuthMethods.md) |  | [optional] 
**usetype** | [**AuthMethodUseTypeResponse**](AuthMethodUseTypeResponse.md) |  | [optional] 

## Example

```python
from autharmor_python.models.response_auth_method import ResponseAuthMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseAuthMethod from a JSON string
response_auth_method_instance = ResponseAuthMethod.from_json(json)
# print the JSON string representation of the object
print ResponseAuthMethod.to_json()

# convert the object into a dict
response_auth_method_dict = response_auth_method_instance.to_dict()
# create an instance of ResponseAuthMethod from a dict
response_auth_method_form_dict = response_auth_method.from_dict(response_auth_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


