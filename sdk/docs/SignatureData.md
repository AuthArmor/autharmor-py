# SignatureData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash_value** | **str** |  | [optional] 
**signature_data** | **str** |  | [optional] 
**auth_method_usetype** | [**AuthMethodUseTypeResponse**](AuthMethodUseTypeResponse.md) |  | [optional] 
**signing_method** | [**SigningMethod**](SigningMethod.md) |  | [optional] 
**auth_method** | [**AuthMethods**](AuthMethods.md) |  | [optional] 
**hash_method** | [**HashTypes**](HashTypes.md) |  | [optional] 

## Example

```python
from autharmor_python.models.signature_data import SignatureData

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureData from a JSON string
signature_data_instance = SignatureData.from_json(json)
# print the JSON string representation of the object
print SignatureData.to_json()

# convert the object into a dict
signature_data_dict = signature_data_instance.to_dict()
# create an instance of SignatureData from a dict
signature_data_form_dict = signature_data.from_dict(signature_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


