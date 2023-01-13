# Project


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_config** | [**Href**](Href.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**customdata** | **object** |  | [optional] 
**devices** | [**List[Href]**](Href.md) |  | [optional] 
**id** | **str** |  | [optional] 
**invitations** | [**List[Href]**](Href.md) |  | [optional] 
**max_devices** | **object** |  | [optional] 
**members** | [**List[Href]**](Href.md) |  | [optional] 
**memberships** | [**List[Href]**](Href.md) |  | [optional] 
**name** | **str** |  | [optional] 
**network_status** | **object** |  | [optional] 
**payment_method** | [**Href**](Href.md) |  | [optional] 
**ssh_keys** | [**List[Href]**](Href.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**volumes** | [**List[Href]**](Href.md) |  | [optional] 
**organization** | [**Organization**](Organization.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from empy.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print Project.to_json()

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_form_dict = project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


