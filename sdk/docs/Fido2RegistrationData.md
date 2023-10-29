# Fido2RegistrationData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attestation_object** | **str** |  | [optional] 
**client_data** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.fido2_registration_data import Fido2RegistrationData

# TODO update the JSON string below
json = "{}"
# create an instance of Fido2RegistrationData from a JSON string
fido2_registration_data_instance = Fido2RegistrationData.from_json(json)
# print the JSON string representation of the object
print Fido2RegistrationData.to_json()

# convert the object into a dict
fido2_registration_data_dict = fido2_registration_data_instance.to_dict()
# create an instance of Fido2RegistrationData from a dict
fido2_registration_data_form_dict = fido2_registration_data.from_dict(fido2_registration_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


