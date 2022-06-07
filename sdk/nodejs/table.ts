// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "./types";
import * as utilities from "./utilities";

import * as pulumiAws from "@pulumi/aws";

export class Table extends pulumi.ComponentResource {
    /** @internal */
    public static readonly __pulumiType = 'aws-dynamodb:index:Table';

    /**
     * Returns true if the given object is an instance of Table.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Table {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Table.__pulumiType;
    }

    public /*out*/ readonly outputs!: pulumi.Output<pulumiAws.dynamodb.Table>;

    /**
     * Create a Table resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TableArgs, opts?: pulumi.ComponentResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["advanced"] = args ? args.advanced : undefined;
            resourceInputs["basic"] = args ? args.basic : undefined;
            resourceInputs["expert"] = args ? args.expert : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["outputs"] = undefined /*out*/;
        } else {
            resourceInputs["outputs"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Table.__pulumiType, name, resourceInputs, opts, true /*remote*/);
    }
}

/**
 * The set of arguments for constructing a Table resource.
 */
export interface TableArgs {
    advanced?: pulumi.Input<inputs.IntermediateTableArgsArgs>;
    basic?: pulumi.Input<inputs.BasicTableArgsArgs>;
    expert?: pulumi.Input<inputs.ExpertTableArgsArgs>;
    type: pulumi.Input<enums.TableType>;
}
