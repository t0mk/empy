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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator

class DeviceCreateInputIpAddressesInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    address_family: Optional[StrictInt] = Field(None, description="Address Family for IP Address")
    cidr: Optional[StrictInt] = Field(None, description="Cidr Size for the IP Block created. Valid values depends on the operating system being provisioned. (28..32 for IPv4 addresses, 124..127 for IPv6 addresses)")
    ip_reservations: Optional[List[StrictStr]] = Field(None, description="UUIDs of any IP reservations to use when assigning IPs")
    public: Optional[StrictBool] = Field(True, description="Address Type for IP Address")
    href: Optional[StrictStr] = None
    __properties = ["address_family", "cidr", "ip_reservations", "public", "href"]

    @validator('address_family')
    def address_family_validate_enum(cls, v):
        if v is None:
            return v

        if v not in (4, 6):
            raise ValueError("must validate the enum values (4, 6)")
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
    def from_json(cls, json_str: str) -> DeviceCreateInputIpAddressesInner:
        """Create an instance of DeviceCreateInputIpAddressesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeviceCreateInputIpAddressesInner:
        """Create an instance of DeviceCreateInputIpAddressesInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DeviceCreateInputIpAddressesInner.parse_obj(obj)

        _obj = DeviceCreateInputIpAddressesInner.parse_obj({
            "address_family": obj.get("address_family"),
            "cidr": obj.get("cidr"),
            "ip_reservations": obj.get("ip_reservations"),
            "public": obj.get("public") if obj.get("public") is not None else True,
            "href": obj.get("href")
        })
        return _obj

