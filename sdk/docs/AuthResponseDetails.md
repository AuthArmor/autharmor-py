# AuthResponseDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**auth_method** | [**ResponseAuthMethod**](ResponseAuthMethod.md) |  | [optional] 
**secure_signed_message** | [**SecureSignedMessage**](SecureSignedMessage.md) |  | [optional] 
**mobile_device_details** | [**MobileDeviceDetails**](MobileDeviceDetails.md) |  | [optional] 
**auth_profile_details** | [**AuthProfileDetails**](AuthProfileDetails.md) |  | [optional] 

## Example

```python
from autharmor_python.models.auth_response_details import AuthResponseDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AuthResponseDetails from a JSON string
auth_response_details_instance = AuthResponseDetails.from_json(json)
# print the JSON string representation of the object
print AuthResponseDetails.to_json()

# convert the object into a dict
auth_response_details_dict = auth_response_details_instance.to_dict()
# create an instance of AuthResponseDetails from a dict
auth_response_details_form_dict = auth_response_details.from_dict(auth_response_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


