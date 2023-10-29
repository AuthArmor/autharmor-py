# GetUserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrolled_auth_methods** | [**List[EnrolledAuthMethod]**](EnrolledAuthMethod.md) |  | [optional] 
**user_id** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] 

## Example

```python
from autharmor_python.models.get_user_response import GetUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserResponse from a JSON string
get_user_response_instance = GetUserResponse.from_json(json)
# print the JSON string representation of the object
print GetUserResponse.to_json()

# convert the object into a dict
get_user_response_dict = get_user_response_instance.to_dict()
# create an instance of GetUserResponse from a dict
get_user_response_form_dict = get_user_response.from_dict(get_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


