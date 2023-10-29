# FinishNewWebauthnUserRegistrationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aa_sig** | **str** |  | 
**authenticator_response_data** | [**Fido2RegistrationData**](Fido2RegistrationData.md) |  | 
**webauthn_client_id** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.finish_new_webauthn_user_registration_request import FinishNewWebauthnUserRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FinishNewWebauthnUserRegistrationRequest from a JSON string
finish_new_webauthn_user_registration_request_instance = FinishNewWebauthnUserRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print FinishNewWebauthnUserRegistrationRequest.to_json()

# convert the object into a dict
finish_new_webauthn_user_registration_request_dict = finish_new_webauthn_user_registration_request_instance.to_dict()
# create an instance of FinishNewWebauthnUserRegistrationRequest from a dict
finish_new_webauthn_user_registration_request_form_dict = finish_new_webauthn_user_registration_request.from_dict(finish_new_webauthn_user_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


