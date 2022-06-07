import * as dynamo from "@pulumi/aws-dynamodb";

export const defaultTable = new dynamo.Table("default-table", {
    type: "default",
});

export const basicTable = new dynamo.Table("basic-table", {
    type: "basic",
    basic: {
        hashKey: {
            name: "id",
            type: "string",
        },
        rangeKey: {
            name: "score",
            type: "number",
        },
    },
});

export const advancedTable = new dynamo.Table("advanced-table", {
    type: "advanced",
    advanced: {
        attributes: [
            {
                name: "UserId",
                type: "S",
            },
            {
                name: "GameTitle",
                type: "S",
            },
            {
                name: "TopScore",
                type: "N",
            },
        ],
        globalSecondaryIndexes: [{
            hashKey: "GameTitle",
            name: "GameTitleIndex",
            nonKeyAttributes: ["UserId"],
            projectionType: "INCLUDE",
            rangeKey: "TopScore",
            readCapacity: 10,
            writeCapacity: 10,
        }],
        hashKey: "UserId",
        provisioned: {
            readCapacity: 10,
            writeCapacity: 10,
        },
        rangeKey: "GameTitle",
        tags: {
            Environment: "production",
            Name: "dynamodb-table-1",
        },
    },
});

export const expertTable = new dynamo.Table("expert-table", {
    type: "expert",
    expert: {
        attributes: [{
            name: "TestTableHashKey",
            type: "S",
        }],
        billingMode: "PAY_PER_REQUEST",
        hashKey: "TestTableHashKey",
        replicas: [
            {
                regionName: "us-east-2",
            },
            {
                regionName: "us-west-1",
            },
        ],
        streamEnabled: true,
        streamViewType: "NEW_AND_OLD_IMAGES",
    },
});
