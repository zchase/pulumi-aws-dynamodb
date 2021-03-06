// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";

import * as pulumiAws from "@pulumi/aws";

/**
 * Arguments for a basic AWS DynamoDB Table.
 */
export interface BasicTableArgsArgs {
    hashKey?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    name?: pulumi.Input<string>;
    provisioned?: pulumi.Input<inputs.ProvisionedTableArgsArgs>;
    rangeKey?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * A map of tags assigned to the resource, including those inherited from the provider .
     */
    tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * Arguments for a basic AWS DynamoDB Table.
 */
export interface ExpertTableArgsArgs {
    /**
     * List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes.
     */
    attributes?: pulumi.Input<pulumi.Input<pulumiAws.types.input.dynamodb.TableAttribute>[]>;
    /**
     * Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
     */
    billingMode?: pulumi.Input<string>;
    /**
     * Describe a GSI for the table;
     * subject to the normal limits on the number of GSIs, projected
     * attributes, etc.
     */
    globalSecondaryIndexes?: pulumi.Input<pulumi.Input<pulumiAws.types.input.dynamodb.TableGlobalSecondaryIndex>[]>;
    /**
     * The name of the hash key in the index; must be
     * defined as an attribute in the resource.
     */
    hashKey?: pulumi.Input<string>;
    /**
     * Describe an LSI on the table;
     * these can only be allocated *at creation* so you cannot change this
     * definition after you have created the resource.
     */
    localSecondaryIndexes?: pulumi.Input<pulumi.Input<pulumiAws.types.input.dynamodb.TableLocalSecondaryIndex>[]>;
    /**
     * The name of the index
     */
    name?: pulumi.Input<string>;
    /**
     * Enable point-in-time recovery options.
     */
    pointInTimeRecovery?: pulumi.Input<pulumiAws.types.input.dynamodb.TablePointInTimeRecovery>;
    /**
     * The name of the range key; must be defined
     */
    rangeKey?: pulumi.Input<string>;
    /**
     * The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
     */
    readCapacity?: pulumi.Input<number>;
    /**
     * Configuration block(s) with [DynamoDB Global Tables V2 (version 2019.11.21)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.V2.html) replication configurations. Detailed below.
     */
    replicas?: pulumi.Input<pulumi.Input<pulumiAws.types.input.dynamodb.TableReplica>[]>;
    /**
     * The time of the point-in-time recovery point to restore.
     */
    restoreDateTime?: pulumi.Input<string>;
    /**
     * The name of the table to restore. Must match the name of an existing table.
     */
    restoreSourceName?: pulumi.Input<string>;
    /**
     * If set, restores table to the most recent point-in-time recovery point.
     */
    restoreToLatestTime?: pulumi.Input<boolean>;
    /**
     * Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn't specified.
     */
    serverSideEncryption?: pulumi.Input<pulumiAws.types.input.dynamodb.TableServerSideEncryption>;
    /**
     * Indicates whether Streams are to be enabled (true) or disabled (false).
     */
    streamEnabled?: pulumi.Input<boolean>;
    /**
     * When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
     */
    streamViewType?: pulumi.Input<string>;
    /**
     * The storage class of the table. Valid values are `STANDARD` and `STANDARD_INFREQUENT_ACCESS`.
     */
    tableClass?: pulumi.Input<string>;
    /**
     * A map of tags to populate on the created table. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
     */
    tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Defines ttl, has two properties, and can only be specified once:
     */
    ttl?: pulumi.Input<pulumiAws.types.input.dynamodb.TableTtl>;
    /**
     * The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
     */
    writeCapacity?: pulumi.Input<number>;
}

/**
 * Arguments for a basic AWS DynamoDB Table.
 */
export interface IntermediateTableArgsArgs {
    /**
     * List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes.
     */
    attributes?: pulumi.Input<pulumi.Input<pulumiAws.types.input.dynamodb.TableAttribute>[]>;
    /**
     * Describe a GSI for the table;
     * subject to the normal limits on the number of GSIs, projected
     * attributes, etc.
     */
    globalSecondaryIndexes?: pulumi.Input<pulumi.Input<pulumiAws.types.input.dynamodb.TableGlobalSecondaryIndex>[]>;
    /**
     * The name of the hash key in the index; must be
     * defined as an attribute in the resource.
     */
    hashKey?: pulumi.Input<string>;
    /**
     * Describe an LSI on the table;
     * these can only be allocated *at creation* so you cannot change this
     * definition after you have created the resource.
     */
    localSecondaryIndexes?: pulumi.Input<pulumi.Input<pulumiAws.types.input.dynamodb.TableLocalSecondaryIndex>[]>;
    name?: pulumi.Input<string>;
    provisioned?: pulumi.Input<inputs.ProvisionedTableArgsArgs>;
    /**
     * The name of the range key; must be defined.
     */
    rangeKey?: pulumi.Input<string>;
    /**
     * A map of tags assigned to the resource, including those inherited from the provider .
     */
    tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The arguments needed for a Provisioned AWS DynamoDB Table. If not provided, then the Table
 * will be provisioned in OnDemand mode.
 */
export interface ProvisionedTableArgsArgs {
    /**
     * The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
     */
    readCapacity: pulumi.Input<number>;
    /**
     * The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
     */
    writeCapacity: pulumi.Input<number>;
}
