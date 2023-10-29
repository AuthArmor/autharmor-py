# UpdateUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_username** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.update_user_request import UpdateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequest from a JSON string
update_user_request_instance = UpdateUserRequest.from_json(json)
# print the JSON string representation of the object
print UpdateUserRequest.to_json()

# convert the object into a dict
update_user_request_dict = update_user_request_instance.to_dict()
# create an instance of UpdateUserRequest from a dict
update_user_request_form_dict = update_user_request.from_dict(update_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


