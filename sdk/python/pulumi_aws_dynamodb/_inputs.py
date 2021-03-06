# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from ._enums import *
import pulumi_aws

__all__ = [
    'BasicTableArgsArgs',
    'ExpertTableArgsArgs',
    'IntermediateTableArgsArgs',
    'ProvisionedTableArgsArgs',
]

@pulumi.input_type
class BasicTableArgsArgs:
    def __init__(__self__, *,
                 hash_key: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioned: Optional[pulumi.Input['ProvisionedTableArgsArgs']] = None,
                 range_key: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Arguments for a basic AWS DynamoDB Table.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags assigned to the resource, including those inherited from the provider .
        """
        if hash_key is not None:
            pulumi.set(__self__, "hash_key", hash_key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if provisioned is not None:
            pulumi.set(__self__, "provisioned", provisioned)
        if range_key is not None:
            pulumi.set(__self__, "range_key", range_key)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="hashKey")
    def hash_key(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "hash_key")

    @hash_key.setter
    def hash_key(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "hash_key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def provisioned(self) -> Optional[pulumi.Input['ProvisionedTableArgsArgs']]:
        return pulumi.get(self, "provisioned")

    @provisioned.setter
    def provisioned(self, value: Optional[pulumi.Input['ProvisionedTableArgsArgs']]):
        pulumi.set(self, "provisioned", value)

    @property
    @pulumi.getter(name="rangeKey")
    def range_key(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "range_key")

    @range_key.setter
    def range_key(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "range_key", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class ExpertTableArgsArgs:
    def __init__(__self__, *,
                 attributes: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableAttributeArgs']]]] = None,
                 billing_mode: Optional[pulumi.Input[str]] = None,
                 global_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableGlobalSecondaryIndexArgs']]]] = None,
                 hash_key: Optional[pulumi.Input[str]] = None,
                 local_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableLocalSecondaryIndexArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 point_in_time_recovery: Optional[pulumi.Input['pulumi_aws.dynamodb.TablePointInTimeRecoveryArgs']] = None,
                 range_key: Optional[pulumi.Input[str]] = None,
                 read_capacity: Optional[pulumi.Input[int]] = None,
                 replicas: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableReplicaArgs']]]] = None,
                 restore_date_time: Optional[pulumi.Input[str]] = None,
                 restore_source_name: Optional[pulumi.Input[str]] = None,
                 restore_to_latest_time: Optional[pulumi.Input[bool]] = None,
                 server_side_encryption: Optional[pulumi.Input['pulumi_aws.dynamodb.TableServerSideEncryptionArgs']] = None,
                 stream_enabled: Optional[pulumi.Input[bool]] = None,
                 stream_view_type: Optional[pulumi.Input[str]] = None,
                 table_class: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 ttl: Optional[pulumi.Input['pulumi_aws.dynamodb.TableTtlArgs']] = None,
                 write_capacity: Optional[pulumi.Input[int]] = None):
        """
        Arguments for a basic AWS DynamoDB Table.
        :param pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableAttributeArgs']]] attributes: List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes.
        :param pulumi.Input[str] billing_mode: Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
        :param pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableGlobalSecondaryIndexArgs']]] global_secondary_indexes: Describe a GSI for the table;
               subject to the normal limits on the number of GSIs, projected
               attributes, etc.
        :param pulumi.Input[str] hash_key: The name of the hash key in the index; must be
               defined as an attribute in the resource.
        :param pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableLocalSecondaryIndexArgs']]] local_secondary_indexes: Describe an LSI on the table;
               these can only be allocated *at creation* so you cannot change this
               definition after you have created the resource.
        :param pulumi.Input[str] name: The name of the index
        :param pulumi.Input['pulumi_aws.dynamodb.TablePointInTimeRecoveryArgs'] point_in_time_recovery: Enable point-in-time recovery options.
        :param pulumi.Input[str] range_key: The name of the range key; must be defined
        :param pulumi.Input[int] read_capacity: The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
        :param pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableReplicaArgs']]] replicas: Configuration block(s) with [DynamoDB Global Tables V2 (version 2019.11.21)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.V2.html) replication configurations. Detailed below.
        :param pulumi.Input[str] restore_date_time: The time of the point-in-time recovery point to restore.
        :param pulumi.Input[str] restore_source_name: The name of the table to restore. Must match the name of an existing table.
        :param pulumi.Input[bool] restore_to_latest_time: If set, restores table to the most recent point-in-time recovery point.
        :param pulumi.Input['pulumi_aws.dynamodb.TableServerSideEncryptionArgs'] server_side_encryption: Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn't specified.
        :param pulumi.Input[bool] stream_enabled: Indicates whether Streams are to be enabled (true) or disabled (false).
        :param pulumi.Input[str] stream_view_type: When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
        :param pulumi.Input[str] table_class: The storage class of the table. Valid values are `STANDARD` and `STANDARD_INFREQUENT_ACCESS`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to populate on the created table. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input['pulumi_aws.dynamodb.TableTtlArgs'] ttl: Defines ttl, has two properties, and can only be specified once:
        :param pulumi.Input[int] write_capacity: The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
        """
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)
        if billing_mode is not None:
            pulumi.set(__self__, "billing_mode", billing_mode)
        if global_secondary_indexes is not None:
            pulumi.set(__self__, "global_secondary_indexes", global_secondary_indexes)
        if hash_key is not None:
            pulumi.set(__self__, "hash_key", hash_key)
        if local_secondary_indexes is not None:
            pulumi.set(__self__, "local_secondary_indexes", local_secondary_indexes)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if point_in_time_recovery is not None:
            pulumi.set(__self__, "point_in_time_recovery", point_in_time_recovery)
        if range_key is not None:
            pulumi.set(__self__, "range_key", range_key)
        if read_capacity is not None:
            pulumi.set(__self__, "read_capacity", read_capacity)
        if replicas is not None:
            pulumi.set(__self__, "replicas", replicas)
        if restore_date_time is not None:
            pulumi.set(__self__, "restore_date_time", restore_date_time)
        if restore_source_name is not None:
            pulumi.set(__self__, "restore_source_name", restore_source_name)
        if restore_to_latest_time is not None:
            pulumi.set(__self__, "restore_to_latest_time", restore_to_latest_time)
        if server_side_encryption is not None:
            pulumi.set(__self__, "server_side_encryption", server_side_encryption)
        if stream_enabled is not None:
            pulumi.set(__self__, "stream_enabled", stream_enabled)
        if stream_view_type is not None:
            pulumi.set(__self__, "stream_view_type", stream_view_type)
        if table_class is not None:
            pulumi.set(__self__, "table_class", table_class)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if write_capacity is not None:
            pulumi.set(__self__, "write_capacity", write_capacity)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableAttributeArgs']]]]:
        """
        List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes.
        """
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableAttributeArgs']]]]):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
        """
        return pulumi.get(self, "billing_mode")

    @billing_mode.setter
    def billing_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "billing_mode", value)

    @property
    @pulumi.getter(name="globalSecondaryIndexes")
    def global_secondary_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableGlobalSecondaryIndexArgs']]]]:
        """
        Describe a GSI for the table;
        subject to the normal limits on the number of GSIs, projected
        attributes, etc.
        """
        return pulumi.get(self, "global_secondary_indexes")

    @global_secondary_indexes.setter
    def global_secondary_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableGlobalSecondaryIndexArgs']]]]):
        pulumi.set(self, "global_secondary_indexes", value)

    @property
    @pulumi.getter(name="hashKey")
    def hash_key(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the hash key in the index; must be
        defined as an attribute in the resource.
        """
        return pulumi.get(self, "hash_key")

    @hash_key.setter
    def hash_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hash_key", value)

    @property
    @pulumi.getter(name="localSecondaryIndexes")
    def local_secondary_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableLocalSecondaryIndexArgs']]]]:
        """
        Describe an LSI on the table;
        these can only be allocated *at creation* so you cannot change this
        definition after you have created the resource.
        """
        return pulumi.get(self, "local_secondary_indexes")

    @local_secondary_indexes.setter
    def local_secondary_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableLocalSecondaryIndexArgs']]]]):
        pulumi.set(self, "local_secondary_indexes", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the index
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="pointInTimeRecovery")
    def point_in_time_recovery(self) -> Optional[pulumi.Input['pulumi_aws.dynamodb.TablePointInTimeRecoveryArgs']]:
        """
        Enable point-in-time recovery options.
        """
        return pulumi.get(self, "point_in_time_recovery")

    @point_in_time_recovery.setter
    def point_in_time_recovery(self, value: Optional[pulumi.Input['pulumi_aws.dynamodb.TablePointInTimeRecoveryArgs']]):
        pulumi.set(self, "point_in_time_recovery", value)

    @property
    @pulumi.getter(name="rangeKey")
    def range_key(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the range key; must be defined
        """
        return pulumi.get(self, "range_key")

    @range_key.setter
    def range_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "range_key", value)

    @property
    @pulumi.getter(name="readCapacity")
    def read_capacity(self) -> Optional[pulumi.Input[int]]:
        """
        The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
        """
        return pulumi.get(self, "read_capacity")

    @read_capacity.setter
    def read_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "read_capacity", value)

    @property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableReplicaArgs']]]]:
        """
        Configuration block(s) with [DynamoDB Global Tables V2 (version 2019.11.21)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.V2.html) replication configurations. Detailed below.
        """
        return pulumi.get(self, "replicas")

    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableReplicaArgs']]]]):
        pulumi.set(self, "replicas", value)

    @property
    @pulumi.getter(name="restoreDateTime")
    def restore_date_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time of the point-in-time recovery point to restore.
        """
        return pulumi.get(self, "restore_date_time")

    @restore_date_time.setter
    def restore_date_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restore_date_time", value)

    @property
    @pulumi.getter(name="restoreSourceName")
    def restore_source_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the table to restore. Must match the name of an existing table.
        """
        return pulumi.get(self, "restore_source_name")

    @restore_source_name.setter
    def restore_source_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restore_source_name", value)

    @property
    @pulumi.getter(name="restoreToLatestTime")
    def restore_to_latest_time(self) -> Optional[pulumi.Input[bool]]:
        """
        If set, restores table to the most recent point-in-time recovery point.
        """
        return pulumi.get(self, "restore_to_latest_time")

    @restore_to_latest_time.setter
    def restore_to_latest_time(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "restore_to_latest_time", value)

    @property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> Optional[pulumi.Input['pulumi_aws.dynamodb.TableServerSideEncryptionArgs']]:
        """
        Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn't specified.
        """
        return pulumi.get(self, "server_side_encryption")

    @server_side_encryption.setter
    def server_side_encryption(self, value: Optional[pulumi.Input['pulumi_aws.dynamodb.TableServerSideEncryptionArgs']]):
        pulumi.set(self, "server_side_encryption", value)

    @property
    @pulumi.getter(name="streamEnabled")
    def stream_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether Streams are to be enabled (true) or disabled (false).
        """
        return pulumi.get(self, "stream_enabled")

    @stream_enabled.setter
    def stream_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "stream_enabled", value)

    @property
    @pulumi.getter(name="streamViewType")
    def stream_view_type(self) -> Optional[pulumi.Input[str]]:
        """
        When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
        """
        return pulumi.get(self, "stream_view_type")

    @stream_view_type.setter
    def stream_view_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stream_view_type", value)

    @property
    @pulumi.getter(name="tableClass")
    def table_class(self) -> Optional[pulumi.Input[str]]:
        """
        The storage class of the table. Valid values are `STANDARD` and `STANDARD_INFREQUENT_ACCESS`.
        """
        return pulumi.get(self, "table_class")

    @table_class.setter
    def table_class(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table_class", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to populate on the created table. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input['pulumi_aws.dynamodb.TableTtlArgs']]:
        """
        Defines ttl, has two properties, and can only be specified once:
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input['pulumi_aws.dynamodb.TableTtlArgs']]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter(name="writeCapacity")
    def write_capacity(self) -> Optional[pulumi.Input[int]]:
        """
        The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
        """
        return pulumi.get(self, "write_capacity")

    @write_capacity.setter
    def write_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "write_capacity", value)


@pulumi.input_type
class IntermediateTableArgsArgs:
    def __init__(__self__, *,
                 attributes: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableAttributeArgs']]]] = None,
                 global_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableGlobalSecondaryIndexArgs']]]] = None,
                 hash_key: Optional[pulumi.Input[str]] = None,
                 local_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableLocalSecondaryIndexArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioned: Optional[pulumi.Input['ProvisionedTableArgsArgs']] = None,
                 range_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Arguments for a basic AWS DynamoDB Table.
        :param pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableAttributeArgs']]] attributes: List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes.
        :param pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableGlobalSecondaryIndexArgs']]] global_secondary_indexes: Describe a GSI for the table;
               subject to the normal limits on the number of GSIs, projected
               attributes, etc.
        :param pulumi.Input[str] hash_key: The name of the hash key in the index; must be
               defined as an attribute in the resource.
        :param pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableLocalSecondaryIndexArgs']]] local_secondary_indexes: Describe an LSI on the table;
               these can only be allocated *at creation* so you cannot change this
               definition after you have created the resource.
        :param pulumi.Input[str] range_key: The name of the range key; must be defined.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags assigned to the resource, including those inherited from the provider .
        """
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)
        if global_secondary_indexes is not None:
            pulumi.set(__self__, "global_secondary_indexes", global_secondary_indexes)
        if hash_key is not None:
            pulumi.set(__self__, "hash_key", hash_key)
        if local_secondary_indexes is not None:
            pulumi.set(__self__, "local_secondary_indexes", local_secondary_indexes)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if provisioned is not None:
            pulumi.set(__self__, "provisioned", provisioned)
        if range_key is not None:
            pulumi.set(__self__, "range_key", range_key)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableAttributeArgs']]]]:
        """
        List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes.
        """
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableAttributeArgs']]]]):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter(name="globalSecondaryIndexes")
    def global_secondary_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableGlobalSecondaryIndexArgs']]]]:
        """
        Describe a GSI for the table;
        subject to the normal limits on the number of GSIs, projected
        attributes, etc.
        """
        return pulumi.get(self, "global_secondary_indexes")

    @global_secondary_indexes.setter
    def global_secondary_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableGlobalSecondaryIndexArgs']]]]):
        pulumi.set(self, "global_secondary_indexes", value)

    @property
    @pulumi.getter(name="hashKey")
    def hash_key(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the hash key in the index; must be
        defined as an attribute in the resource.
        """
        return pulumi.get(self, "hash_key")

    @hash_key.setter
    def hash_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hash_key", value)

    @property
    @pulumi.getter(name="localSecondaryIndexes")
    def local_secondary_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableLocalSecondaryIndexArgs']]]]:
        """
        Describe an LSI on the table;
        these can only be allocated *at creation* so you cannot change this
        definition after you have created the resource.
        """
        return pulumi.get(self, "local_secondary_indexes")

    @local_secondary_indexes.setter
    def local_secondary_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.dynamodb.TableLocalSecondaryIndexArgs']]]]):
        pulumi.set(self, "local_secondary_indexes", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def provisioned(self) -> Optional[pulumi.Input['ProvisionedTableArgsArgs']]:
        return pulumi.get(self, "provisioned")

    @provisioned.setter
    def provisioned(self, value: Optional[pulumi.Input['ProvisionedTableArgsArgs']]):
        pulumi.set(self, "provisioned", value)

    @property
    @pulumi.getter(name="rangeKey")
    def range_key(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the range key; must be defined.
        """
        return pulumi.get(self, "range_key")

    @range_key.setter
    def range_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "range_key", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class ProvisionedTableArgsArgs:
    def __init__(__self__, *,
                 read_capacity: pulumi.Input[int],
                 write_capacity: pulumi.Input[int]):
        """
        The arguments needed for a Provisioned AWS DynamoDB Table. If not provided, then the Table
        will be provisioned in OnDemand mode.

        :param pulumi.Input[int] read_capacity: The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
        :param pulumi.Input[int] write_capacity: The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
        """
        pulumi.set(__self__, "read_capacity", read_capacity)
        pulumi.set(__self__, "write_capacity", write_capacity)

    @property
    @pulumi.getter(name="readCapacity")
    def read_capacity(self) -> pulumi.Input[int]:
        """
        The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
        """
        return pulumi.get(self, "read_capacity")

    @read_capacity.setter
    def read_capacity(self, value: pulumi.Input[int]):
        pulumi.set(self, "read_capacity", value)

    @property
    @pulumi.getter(name="writeCapacity")
    def write_capacity(self) -> pulumi.Input[int]:
        """
        The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
        """
        return pulumi.get(self, "write_capacity")

    @write_capacity.setter
    def write_capacity(self, value: pulumi.Input[int]):
        pulumi.set(self, "write_capacity", value)


