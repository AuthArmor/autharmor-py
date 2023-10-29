# LocationData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **str** |  | [optional] 
**longitude** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.location_data import LocationData

# TODO update the JSON string below
json = "{}"
# create an instance of LocationData from a JSON string
location_data_instance = LocationData.from_json(json)
# print the JSON string representation of the object
print LocationData.to_json()

# convert the object into a dict
location_data_dict = location_data_instance.to_dict()
# create an instance of LocationData from a dict
location_data_form_dict = location_data.from_dict(location_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


