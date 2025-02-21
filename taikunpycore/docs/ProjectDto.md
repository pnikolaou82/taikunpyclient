# ProjectDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**project_name** | **str** |  | 

## Example

```python
from taikunpycore.models.project_dto import ProjectDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDto from a JSON string
project_dto_instance = ProjectDto.from_json(json)
# print the JSON string representation of the object
print(ProjectDto.to_json())

# convert the object into a dict
project_dto_dict = project_dto_instance.to_dict()
# create an instance of ProjectDto from a dict
project_dto_from_dict = ProjectDto.from_dict(project_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


