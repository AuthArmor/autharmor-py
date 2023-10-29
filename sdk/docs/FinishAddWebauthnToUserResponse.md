# FinishAddWebauthnToUserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_validation_token** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.finish_add_webauthn_to_user_response import FinishAddWebauthnToUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FinishAddWebauthnToUserResponse from a JSON string
finish_add_webauthn_to_user_response_instance = FinishAddWebauthnToUserResponse.from_json(json)
# print the JSON string representation of the object
print FinishAddWebauthnToUserResponse.to_json()

# convert the object into a dict
finish_add_webauthn_to_user_response_dict = finish_add_webauthn_to_user_response_instance.to_dict()
# create an instance of FinishAddWebauthnToUserResponse from a dict
finish_add_webauthn_to_user_response_form_dict = finish_add_webauthn_to_user_response.from_dict(finish_add_webauthn_to_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


