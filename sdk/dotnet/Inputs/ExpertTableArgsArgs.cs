// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsDynamoDB.Inputs
{

    /// <summary>
    /// Arguments for a basic AWS DynamoDB Table.
    /// </summary>
    public sealed class ExpertTableArgsArgs : Pulumi.ResourceArgs
    {
        [Input("attributes")]
        private InputList<Pulumi.Aws.DynamoDB.Inputs.TableAttributeArgs>? _attributes;

        /// <summary>
        /// List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes.
        /// </summary>
        public InputList<Pulumi.Aws.DynamoDB.Inputs.TableAttributeArgs> Attributes
        {
            get => _attributes ?? (_attributes = new InputList<Pulumi.Aws.DynamoDB.Inputs.TableAttributeArgs>());
            set => _attributes = value;
        }

        /// <summary>
        /// Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
        /// </summary>
        [Input("billingMode")]
        public Input<string>? BillingMode { get; set; }

        [Input("globalSecondaryIndexes")]
        private InputList<Pulumi.Aws.DynamoDB.Inputs.TableGlobalSecondaryIndexArgs>? _globalSecondaryIndexes;

        /// <summary>
        /// Describe a GSI for the table;
        /// subject to the normal limits on the number of GSIs, projected
        /// attributes, etc.
        /// </summary>
        public InputList<Pulumi.Aws.DynamoDB.Inputs.TableGlobalSecondaryIndexArgs> GlobalSecondaryIndexes
        {
            get => _globalSecondaryIndexes ?? (_globalSecondaryIndexes = new InputList<Pulumi.Aws.DynamoDB.Inputs.TableGlobalSecondaryIndexArgs>());
            set => _globalSecondaryIndexes = value;
        }

        /// <summary>
        /// The name of the hash key in the index; must be
        /// defined as an attribute in the resource.
        /// </summary>
        [Input("hashKey")]
        public Input<string>? HashKey { get; set; }

        [Input("localSecondaryIndexes")]
        private InputList<Pulumi.Aws.DynamoDB.Inputs.TableLocalSecondaryIndexArgs>? _localSecondaryIndexes;

        /// <summary>
        /// Describe an LSI on the table;
        /// these can only be allocated *at creation* so you cannot change this
        /// definition after you have created the resource.
        /// </summary>
        public InputList<Pulumi.Aws.DynamoDB.Inputs.TableLocalSecondaryIndexArgs> LocalSecondaryIndexes
        {
            get => _localSecondaryIndexes ?? (_localSecondaryIndexes = new InputList<Pulumi.Aws.DynamoDB.Inputs.TableLocalSecondaryIndexArgs>());
            set => _localSecondaryIndexes = value;
        }

        /// <summary>
        /// The name of the index
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Enable point-in-time recovery options.
        /// </summary>
        [Input("pointInTimeRecovery")]
        public Input<Pulumi.Aws.DynamoDB.Inputs.TablePointInTimeRecoveryArgs>? PointInTimeRecovery { get; set; }

        /// <summary>
        /// The name of the range key; must be defined
        /// </summary>
        [Input("rangeKey")]
        public Input<string>? RangeKey { get; set; }

        /// <summary>
        /// The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
        /// </summary>
        [Input("readCapacity")]
        public Input<int>? ReadCapacity { get; set; }

        [Input("replicas")]
        private InputList<Pulumi.Aws.DynamoDB.Inputs.TableReplicaArgs>? _replicas;

        /// <summary>
        /// Configuration block(s) with [DynamoDB Global Tables V2 (version 2019.11.21)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.V2.html) replication configurations. Detailed below.
        /// </summary>
        public InputList<Pulumi.Aws.DynamoDB.Inputs.TableReplicaArgs> Replicas
        {
            get => _replicas ?? (_replicas = new InputList<Pulumi.Aws.DynamoDB.Inputs.TableReplicaArgs>());
            set => _replicas = value;
        }

        /// <summary>
        /// The time of the point-in-time recovery point to restore.
        /// </summary>
        [Input("restoreDateTime")]
        public Input<string>? RestoreDateTime { get; set; }

        /// <summary>
        /// The name of the table to restore. Must match the name of an existing table.
        /// </summary>
        [Input("restoreSourceName")]
        public Input<string>? RestoreSourceName { get; set; }

        /// <summary>
        /// If set, restores table to the most recent point-in-time recovery point.
        /// </summary>
        [Input("restoreToLatestTime")]
        public Input<bool>? RestoreToLatestTime { get; set; }

        /// <summary>
        /// Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn't specified.
        /// </summary>
        [Input("serverSideEncryption")]
        public Input<Pulumi.Aws.DynamoDB.Inputs.TableServerSideEncryptionArgs>? ServerSideEncryption { get; set; }

        /// <summary>
        /// Indicates whether Streams are to be enabled (true) or disabled (false).
        /// </summary>
        [Input("streamEnabled")]
        public Input<bool>? StreamEnabled { get; set; }

        /// <summary>
        /// When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
        /// </summary>
        [Input("streamViewType")]
        public Input<string>? StreamViewType { get; set; }

        /// <summary>
        /// The storage class of the table. Valid values are `STANDARD` and `STANDARD_INFREQUENT_ACCESS`.
        /// </summary>
        [Input("tableClass")]
        public Input<string>? TableClass { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to populate on the created table. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// Defines ttl, has two properties, and can only be specified once:
        /// </summary>
        [Input("ttl")]
        public Input<Pulumi.Aws.DynamoDB.Inputs.TableTtlArgs>? Ttl { get; set; }

        /// <summary>
        /// The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
        /// </summary>
        [Input("writeCapacity")]
        public Input<int>? WriteCapacity { get; set; }

        public ExpertTableArgsArgs()
        {
        }
    }
}