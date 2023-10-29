# UserAuthHistoryPageInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currnet_page_number** | **int** |  | [optional] 
**currnet_page_size** | **int** |  | [optional] 
**total_page_count** | **int** |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from autharmor_python.models.user_auth_history_page_info import UserAuthHistoryPageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserAuthHistoryPageInfo from a JSON string
user_auth_history_page_info_instance = UserAuthHistoryPageInfo.from_json(json)
# print the JSON string representation of the object
print UserAuthHistoryPageInfo.to_json()

# convert the object into a dict
user_auth_history_page_info_dict = user_auth_history_page_info_instance.to_dict()
# create an instance of UserAuthHistoryPageInfo from a dict
user_auth_history_page_info_form_dict = user_auth_history_page_info.from_dict(user_auth_history_page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


