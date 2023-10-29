# GetUserAuthHistoryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_history_records** | [**List[GetAuthRequestResponse]**](GetAuthRequestResponse.md) |  | [optional] 
**page_info** | [**UserAuthHistoryPageInfo**](UserAuthHistoryPageInfo.md) |  | [optional] 

## Example

```python
from autharmor_python.models.get_user_auth_history_response import GetUserAuthHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserAuthHistoryResponse from a JSON string
get_user_auth_history_response_instance = GetUserAuthHistoryResponse.from_json(json)
# print the JSON string representation of the object
print GetUserAuthHistoryResponse.to_json()

# convert the object into a dict
get_user_auth_history_response_dict = get_user_auth_history_response_instance.to_dict()
# create an instance of GetUserAuthHistoryResponse from a dict
get_user_auth_history_response_form_dict = get_user_auth_history_response.from_dict(get_user_auth_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


