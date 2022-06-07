# Pulumi AWS DynamoDB Component

This Pulumi Multi Language Component is a prototype Component exploring the idea to provide a different
set of arguments to specified "difficulty" levels.

## Default

The "defaul" difficulty provides a DynamoDB Table that is "PAY_PER_REQUEST" and has a Hash Key of "id".

```typescript
import * as dynamo from "@pulumi/aws-dynamodb";

export const defaultTable = new dynamo.Table("default-table", {
    type: "default",
});
```

## Basic

The "basic" difficulty provides a DynamoDB Table with a specified Hash and Range Keys.

```typescript
import * as dynamo from "@pulumi/aws-dynamodb";

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
```

## Advanced

The "advance" difficulty provides a DynamoDB Table with a specified Hash and Range Keys as well as supports
secondary indexes.

```typescript
import * as dynamo from "@pulumi/aws-dynamodb";

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
```

## Expert

The "expert" difficulty provides the full set of arguments to a DynamoDB Table resource.

```typescript
import * as dynamo from "@pulumi/aws-dynamodb";

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
```

## Development

### Prerequisites

- Go 1.17
- Pulumi CLI
- Node.js (to build the Node.js SDK)
- Yarn (to build the Node.js SDK)
- Python 3.6+ (to build the Python SDK)
- .NET Core SDK (to build the .NET SDK)

### Build and Test

```bash
# Build and install the provider (plugin copied to $GOPATH/bin)
make install_provider

# Regenerate SDKs
make generate

# Test Node.js SDK
$ make install_nodejs_sdk
$ cd examples/simple
$ yarn install
$ yarn link @pulumi/aws-dynamodb
$ pulumi stack init test
$ pulumi config set aws:region us-east-1
$ pulumi up
```
