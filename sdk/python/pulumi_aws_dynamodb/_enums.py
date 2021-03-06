# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'TableKeyType',
    'TableType',
]


class TableKeyType(str, Enum):
    """
    The type of key for your DynamoDB Table.
    """
    STRING = "string"
    NUMBER = "number"


class TableType(str, Enum):
    """
    The type of DynamoDB Table.
    """
    DEFAULT = "default"
    BASIC = "basic"
    ADVANCED = "advanced"
    EXPERT = "expert"
