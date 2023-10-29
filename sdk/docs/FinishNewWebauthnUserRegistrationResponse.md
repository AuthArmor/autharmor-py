# FinishNewWebauthnUserRegistrationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_validation_token** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.finish_new_webauthn_user_registration_response import FinishNewWebauthnUserRegistrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FinishNewWebauthnUserRegistrationResponse from a JSON string
finish_new_webauthn_user_registration_response_instance = FinishNewWebauthnUserRegistrationResponse.from_json(json)
# print the JSON string representation of the object
print FinishNewWebauthnUserRegistrationResponse.to_json()

# convert the object into a dict
finish_new_webauthn_user_registration_response_dict = finish_new_webauthn_user_registration_response_instance.to_dict()
# create an instance of FinishNewWebauthnUserRegistrationResponse from a dict
finish_new_webauthn_user_registration_response_form_dict = finish_new_webauthn_user_registration_response.from_dict(finish_new_webauthn_user_registration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


