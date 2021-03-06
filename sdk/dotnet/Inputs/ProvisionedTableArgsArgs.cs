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
    /// The arguments needed for a Provisioned AWS DynamoDB Table. If not provided, then the Table
    /// will be provisioned in OnDemand mode.
    /// </summary>
    public sealed class ProvisionedTableArgsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
        /// </summary>
        [Input("readCapacity", required: true)]
        public Input<int> ReadCapacity { get; set; } = null!;

        /// <summary>
        /// The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
        /// </summary>
        [Input("writeCapacity", required: true)]
        public Input<int> WriteCapacity { get; set; } = null!;

        public ProvisionedTableArgsArgs()
        {
        }
    }
}
