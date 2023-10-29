# FinishAddWebauthnToUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aa_sig** | **str** |  | 
**authenticator_response_data** | [**Fido2RegistrationData**](Fido2RegistrationData.md) |  | 
**webauthn_client_id** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.finish_add_webauthn_to_user_request import FinishAddWebauthnToUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FinishAddWebauthnToUserRequest from a JSON string
finish_add_webauthn_to_user_request_instance = FinishAddWebauthnToUserRequest.from_json(json)
# print the JSON string representation of the object
print FinishAddWebauthnToUserRequest.to_json()

# convert the object into a dict
finish_add_webauthn_to_user_request_dict = finish_add_webauthn_to_user_request_instance.to_dict()
# create an instance of FinishAddWebauthnToUserRequest from a dict
finish_add_webauthn_to_user_request_form_dict = finish_add_webauthn_to_user_request.from_dict(finish_add_webauthn_to_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


