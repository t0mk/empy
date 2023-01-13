# coding: utf-8

"""
    Metal API

    desc  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr, validator

class PlanSpecsDrivesInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    count: Optional[StrictInt] = None
    type: Optional[StrictStr] = None
    size: Optional[StrictStr] = None
    category: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    __properties = ["count", "type", "size", "category", "href"]

    @validator('type')
    def type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('HDD', 'SSD', 'NVME'):
            raise ValueError("must validate the enum values ('HDD', 'SSD', 'NVME')")
        return v

    @validator('category')
    def category_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('boot', 'cache', 'storage'):
            raise ValueError("must validate the enum values ('boot', 'cache', 'storage')")
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PlanSpecsDrivesInner:
        """Create an instance of PlanSpecsDrivesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlanSpecsDrivesInner:
        """Create an instance of PlanSpecsDrivesInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PlanSpecsDrivesInner.parse_obj(obj)

        _obj = PlanSpecsDrivesInner.parse_obj({
            "count": obj.get("count"),
            "type": obj.get("type"),
            "size": obj.get("size"),
            "category": obj.get("category"),
            "href": obj.get("href")
        })
        return _obj
