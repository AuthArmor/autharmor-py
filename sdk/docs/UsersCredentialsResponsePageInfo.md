# UsersCredentialsResponsePageInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currnet_page_number** | **int** |  | [optional] 
**currnet_page_size** | **int** |  | [optional] 
**total_page_count** | **int** |  | [optional] 
**total_record_count** | **int** |  | [optional] 

## Example

```python
from autharmor_python.models.users_credentials_response_page_info import UsersCredentialsResponsePageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCredentialsResponsePageInfo from a JSON string
users_credentials_response_page_info_instance = UsersCredentialsResponsePageInfo.from_json(json)
# print the JSON string representation of the object
print UsersCredentialsResponsePageInfo.to_json()

# convert the object into a dict
users_credentials_response_page_info_dict = users_credentials_response_page_info_instance.to_dict()
# create an instance of UsersCredentialsResponsePageInfo from a dict
users_credentials_response_page_info_form_dict = users_credentials_response_page_info.from_dict(users_credentials_response_page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


