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

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator
from empy.models.device_create_input_ip_addresses_inner import DeviceCreateInputIpAddressesInner
from empy.models.ssh_key_input import SSHKeyInput

class DeviceCreateInMetroInput(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    metro: StrictStr = Field(..., description="Metro code or ID of where the instance should be provisioned in. Either metro or facility must be provided.")
    href: Optional[StrictStr] = None
    always_pxe: Optional[StrictBool] = Field(None, description="When True, devices with a `custom_ipxe` OS will always boot to iPXE. The default setting of False ensures that iPXE will be used on only the first boot.")
    billing_cycle: Optional[StrictStr] = Field(None, description="The billing cycle of the device.")
    customdata: Optional[Dict[str, Any]] = Field(None, description="Customdata is an arbitrary JSON value that can be accessed via the metadata service.")
    description: Optional[StrictStr] = Field(None, description="Any description of the device or how it will be used. This may be used to inform other API consumers with project access.")
    features: Optional[List[StrictStr]] = Field(None, description="The features attribute allows you to optionally specify what features your server should have.  In the API shorthand syntax, all features listed are `required`:  ``` { \"features\": [\"tpm\"] } ```  Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a `preferred` value. The request will not fail if we have no servers with that feature in our inventory. The API offers an alternative syntax for mixing preferred and required features:  ``` { \"features\": { \"tpm\": \"required\", \"raid\": \"preferred\" } } ```  The request will only fail if there are no available servers matching the required `tpm` criteria.")
    hardware_reservation_id: Optional[StrictStr] = Field(None, description="The Hardware Reservation UUID to provision. Alternatively, `next-available` can be specified to select from any of the available hardware reservations. An error will be returned if the requested reservation option is not available.  See [Reserved Hardware](https://metal.equinix.com/developers/docs/deploy/reserved/) for more details.")
    hostname: Optional[StrictStr] = Field(None, description="The hostname to use within the operating system. The same hostname may be used on multiple devices within a project.")
    ip_addresses: Optional[List[DeviceCreateInputIpAddressesInner]] = Field([{"address_family":4,"public":True},{"address_family":4,"public":False},{"address_family":6,"public":True}], description="The `ip_addresses attribute will allow you to specify the addresses you want created with your device.  The default value configures public IPv4, public IPv6, and private IPv4.  Private IPv4 address is required. When specifying `ip_addresses`, one of the array items must enable private IPv4.  Some operating systems require public IPv4 address. In those cases you will receive an error message if public IPv4 is not enabled.  For example, to only configure your server with a private IPv4 address, you can send `{ \"ip_addresses\": [{ \"address_family\": 4, \"public\": False }] }`.  It is possible to request a subnet size larger than a `/30` by assigning addresses using the UUID(s) of ip_reservations in your project.  For example, `{ \"ip_addresses\": [..., {\"address_family\": 4, \"public\": True, \"ip_reservations\": [\"uuid1\", \"uuid2\"]}] }`  To access a server without public IPs, you can use our Out-of-Band console access (SOS) or proxy through another server in the project with public IPs enabled.")
    ipxe_script_url: Optional[StrictStr] = Field(None, description="When set, the device will chainload an iPXE Script at boot fetched from the supplied URL.  See [Custom iPXE](https://metal.equinix.com/developers/docs/operating-systems/custom-ipxe/) for more details.")
    locked: Optional[StrictBool] = Field(False, description="Whether the device should be locked, preventing accidental deletion.")
    no_ssh_keys: Optional[StrictBool] = Field(False, description="Overrides default behaviour of attaching all of the organization members ssh keys and project ssh keys to device if no specific keys specified")
    operating_system: StrictStr = Field(..., description="The slug of the operating system to provision. Check the Equinix Metal operating system documentation for rules that may be imposed per operating system, including restrictions on IP address options and device plans.")
    plan: StrictStr = Field(..., description="The slug of the device plan to provision.")
    private_ipv4_subnet_size: Optional[StrictInt] = Field(28, description="Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device.")
    project_ssh_keys: Optional[List[StrictStr]] = Field(None, description="A list of UUIDs identifying the device parent project that should be authorized to access this device (typically via /root/.ssh/authorized_keys). These keys will also appear in the device metadata.  If no SSH keys are specified (`user_ssh_keys`, `project_ssh_keys`, and `ssh_keys` are all empty lists or omitted), all parent project keys, parent project members keys and organization members keys will be included. This behaviour can be changed with 'no_ssh_keys' option to omit any SSH key being added. ")
    public_ipv4_subnet_size: Optional[StrictInt] = Field(31, description="Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device. Your project must have addresses available for a non-default request.")
    spot_instance: Optional[StrictBool] = Field(None, description="Create a spot instance. Spot instances are created with a maximum bid price. If the bid price is not met, the spot instance will be terminated as indicated by the `termination_time` field.")
    spot_price_max: Optional[StrictFloat] = Field(None, description="The maximum amount to bid for a spot instance.")
    ssh_keys: Optional[List[SSHKeyInput]] = Field(None, description="A list of new or existing project ssh_keys that should be authorized to access this device (typically via /root/.ssh/authorized_keys). These keys will also appear in the device metadata.  These keys are added in addition to any keys defined by   `project_ssh_keys` and `user_ssh_keys`. ")
    tags: Optional[List[StrictStr]] = None
    termination_time: Optional[datetime] = None
    user_ssh_keys: Optional[List[StrictStr]] = Field(None, description="A list of UUIDs identifying the users that should be authorized to access this device (typically via /root/.ssh/authorized_keys).  These keys will also appear in the device metadata.  The users must be members of the project or organization.  If no SSH keys are specified (`user_ssh_keys`, `project_ssh_keys`, and `ssh_keys` are all empty lists or omitted), all parent project keys, parent project members keys and organization members keys will be included. This behaviour can be changed with 'no_ssh_keys' option to omit any SSH key being added. ")
    userdata: Optional[StrictStr] = Field(None, description="The userdata presented in the metadata service for this device.  Userdata is fetched and interpreted by the operating system installed on the device. Acceptable formats are determined by the operating system, with the exception of a special iPXE enabling syntax which is handled before the operating system starts.  See [Server User Data](https://metal.equinix.com/developers/docs/servers/user-data/) and [Provisioning with Custom iPXE](https://metal.equinix.com/developers/docs/operating-systems/custom-ipxe/#provisioning-with-custom-ipxe) for more details.")
    __properties = ["metro", "href", "always_pxe", "billing_cycle", "customdata", "description", "features", "hardware_reservation_id", "hostname", "ip_addresses", "ipxe_script_url", "locked", "no_ssh_keys", "operating_system", "plan", "private_ipv4_subnet_size", "project_ssh_keys", "public_ipv4_subnet_size", "spot_instance", "spot_price_max", "ssh_keys", "tags", "termination_time", "user_ssh_keys", "userdata"]

    @validator('billing_cycle')
    def billing_cycle_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('hourly', 'daily', 'monthly', 'yearly'):
            raise ValueError("must validate the enum values ('hourly', 'daily', 'monthly', 'yearly')")
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
    def from_json(cls, json_str: str) -> DeviceCreateInMetroInput:
        """Create an instance of DeviceCreateInMetroInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in ip_addresses (list)
        _items = []
        if self.ip_addresses:
            for _item in self.ip_addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ip_addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ssh_keys (list)
        _items = []
        if self.ssh_keys:
            for _item in self.ssh_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ssh_keys'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeviceCreateInMetroInput:
        """Create an instance of DeviceCreateInMetroInput from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DeviceCreateInMetroInput.parse_obj(obj)

        _obj = DeviceCreateInMetroInput.parse_obj({
            "metro": obj.get("metro"),
            "href": obj.get("href"),
            "always_pxe": obj.get("always_pxe"),
            "billing_cycle": obj.get("billing_cycle"),
            "customdata": obj.get("customdata"),
            "description": obj.get("description"),
            "features": obj.get("features"),
            "hardware_reservation_id": obj.get("hardware_reservation_id"),
            "hostname": obj.get("hostname"),
            "ip_addresses": [DeviceCreateInputIpAddressesInner.from_dict(_item) for _item in obj.get("ip_addresses")] if obj.get("ip_addresses") is not None else None,
            "ipxe_script_url": obj.get("ipxe_script_url"),
            "locked": obj.get("locked") if obj.get("locked") is not None else False,
            "no_ssh_keys": obj.get("no_ssh_keys") if obj.get("no_ssh_keys") is not None else False,
            "operating_system": obj.get("operating_system"),
            "plan": obj.get("plan"),
            "private_ipv4_subnet_size": obj.get("private_ipv4_subnet_size") if obj.get("private_ipv4_subnet_size") is not None else 28,
            "project_ssh_keys": obj.get("project_ssh_keys"),
            "public_ipv4_subnet_size": obj.get("public_ipv4_subnet_size") if obj.get("public_ipv4_subnet_size") is not None else 31,
            "spot_instance": obj.get("spot_instance"),
            "spot_price_max": obj.get("spot_price_max"),
            "ssh_keys": [SSHKeyInput.from_dict(_item) for _item in obj.get("ssh_keys")] if obj.get("ssh_keys") is not None else None,
            "tags": obj.get("tags"),
            "termination_time": obj.get("termination_time"),
            "user_ssh_keys": obj.get("user_ssh_keys"),
            "userdata": obj.get("userdata")
        })
        return _obj

