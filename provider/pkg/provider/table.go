// Copyright 2016-2021, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package provider

import (
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/dynamodb"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type tableType string

const (
	tableIdentifier = "aws-dynamodb:index:Table"

	defaultTableType  tableType = "default"
	basicTableType    tableType = "basic"
	advancedTableType tableType = "advanced"
	expertTableType   tableType = "expert"
)

type provisionedTableArgs struct {
	ReadCapacity  pulumi.IntInput `pulumi:"readCapacity"`
	WriteCapacity pulumi.IntInput `pulumi:"writeCapacity"`
}

type basicTableKeyArgs struct {
	Name string `pulumi:"name"`
	Type string `pulumi:"type"`
}

func (b basicTableKeyArgs) DynamoType() string {
	if b.Type == "string" {
		return "S"
	}

	return "N"
}

type basicTableArgs struct {
	HashKey     basicTableKeyArgs     `pulumi:"hashKey"`
	Name        pulumi.StringInput    `pulumi:"name"`
	Provisioned *provisionedTableArgs `pulumi:"provisioned"`
	RangeKey    basicTableKeyArgs     `pulumi:"rangeKey"`
	Tags        pulumi.StringMapInput `pulumi:"tags"`
}

func (b basicTableArgs) ToTableArgs(args *dynamodb.TableArgs) *dynamodb.TableArgs {
	args.Name = b.Name
	args.Tags = b.Tags
	args.BillingMode = pulumi.String("PAY_PER_REQUEST")

	hashKey := &dynamodb.TableAttributeArgs{
		Name: pulumi.String(b.HashKey.Name),
		Type: pulumi.String(b.HashKey.DynamoType()),
	}

	rangeKey := &dynamodb.TableAttributeArgs{
		Name: pulumi.String(b.RangeKey.Name),
		Type: pulumi.String(b.RangeKey.DynamoType()),
	}

	args.HashKey = pulumi.String(b.HashKey.Name)
	args.Attributes = dynamodb.TableAttributeArray{
		hashKey,
	}

	if b.RangeKey.Name != "" {
		args.RangeKey = pulumi.String(b.RangeKey.Name)
		args.Attributes = dynamodb.TableAttributeArray{
			hashKey,
			rangeKey,
		}
	}

	if b.Provisioned != nil {
		args.BillingMode = pulumi.String("PROVISIONED")
		args.ReadCapacity = b.Provisioned.ReadCapacity
		args.WriteCapacity = b.Provisioned.WriteCapacity
	}

	return args
}

type advancedTableArgs struct {
	Attributes             dynamodb.TableAttributeArrayInput            `pulumi:"attributes"`
	GlobalSecondaryIndexes dynamodb.TableGlobalSecondaryIndexArrayInput `pulumi:"globalSecondaryIndexes"`
	HashKey                pulumi.StringInput                           `pulumi:"hashKey"`
	LocalSecondaryIndexes  dynamodb.TableLocalSecondaryIndexArrayInput  `pulumi:"localSecondaryIndexes"`
	Name                   pulumi.StringInput                           `pulumi:"name"`
	Provisioned            *provisionedTableArgs                        `pulumi:"provisioned"`
	RangeKey               pulumi.StringInput                           `pulumi:"rangeKey"`
	Tags                   pulumi.StringMapInput                        `pulumi:"tags"`
}

func (i advancedTableArgs) ToTableArgs(args *dynamodb.TableArgs) *dynamodb.TableArgs {
	args.Attributes = i.Attributes
	args.GlobalSecondaryIndexes = i.GlobalSecondaryIndexes
	args.HashKey = i.HashKey
	args.LocalSecondaryIndexes = i.LocalSecondaryIndexes
	args.Name = i.Name
	args.RangeKey = i.RangeKey
	args.Tags = i.Tags
	args.BillingMode = pulumi.String("PAY_PER_REQUEST")

	if i.Provisioned != nil {
		args.BillingMode = pulumi.String("PROVISIONED")
		args.ReadCapacity = i.Provisioned.ReadCapacity
		args.WriteCapacity = i.Provisioned.WriteCapacity
	}

	return args
}

type expertTableArgs struct {
	Attributes             dynamodb.TableAttributeArrayInput            `pulumi:"attributes"`
	BillingMode            pulumi.StringInput                           `pulumi:"billingMode"`
	GlobalSecondaryIndexes dynamodb.TableGlobalSecondaryIndexArrayInput `pulumi:"globalSecondaryIndexes"`
	HashKey                pulumi.StringInput                           `pulumi:"hashKey"`
	LocalSecondaryIndexes  dynamodb.TableLocalSecondaryIndexArrayInput  `pulumi:"localSecondaryIndexes"`
	Name                   pulumi.StringInput                           `pulumi:"name"`
	PointInTimeRecovery    *dynamodb.TablePointInTimeRecoveryArgs       `pulumi:"pointInTimeRecovery"`
	RangeKey               pulumi.StringInput                           `pulumi:"rangeKey"`
	ReadCapacity           pulumi.IntInput                              `pulumi:"readCapacity"`
	Replicas               dynamodb.TableReplicaArrayInput              `pulumi:"replicas"`
	RestoreDateTime        pulumi.StringInput                           `pulumi:"restoreDateTime"`
	RestoreSourceName      pulumi.StringInput                           `pulumi:"restoreSourceName"`
	RestoreToLatestTime    pulumi.BoolInput                             `pulumi:"restoreToLatestTime"`
	ServerSideEncryption   *dynamodb.TableServerSideEncryptionArgs      `pulumi:"serverSideEncryption"`
	StreamEnabled          pulumi.BoolInput                             `pulumi:"streamEnabled"`
	StreamViewType         pulumi.StringInput                           `pulumi:"streamViewType"`
	TableClass             pulumi.StringInput                           `pulumi:"tableClass"`
	Tags                   pulumi.StringMapInput                        `pulumi:"tags"`
	TTL                    *dynamodb.TableTtlArgs                       `pulumi:"ttl"`
	WriteCapacity          pulumi.IntInput                              `pulumi:"writeCapacity"`
}

func (e expertTableArgs) ToTableArgs(args *dynamodb.TableArgs) *dynamodb.TableArgs {
	args.Attributes = e.Attributes
	args.BillingMode = e.BillingMode
	args.GlobalSecondaryIndexes = e.GlobalSecondaryIndexes
	args.HashKey = e.HashKey
	args.LocalSecondaryIndexes = e.LocalSecondaryIndexes
	args.Name = e.Name
	args.PointInTimeRecovery = e.PointInTimeRecovery
	args.RangeKey = e.RangeKey
	args.ReadCapacity = e.ReadCapacity
	args.Replicas = e.Replicas
	args.RestoreDateTime = e.RestoreDateTime
	args.RestoreSourceName = e.RestoreSourceName
	args.RestoreToLatestTime = e.RestoreToLatestTime
	args.ServerSideEncryption = e.ServerSideEncryption
	args.StreamEnabled = e.StreamEnabled
	args.StreamViewType = e.StreamViewType
	args.TableClass = e.TableClass
	args.Tags = e.Tags
	args.Ttl = e.TTL
	args.WriteCapacity = e.WriteCapacity
	return args
}

type TableArgs struct {
	Type     tableType         `pulumi:"type"`
	Basic    basicTableArgs    `pulumi:"basic"`
	Advanced advancedTableArgs `pulumi:"advanced"`
	Expert   expertTableArgs   `pulumi:"expert"`
}

type Table struct {
	pulumi.ResourceState

	Outputs *dynamodb.Table `pulumi:"outputs"`
}

func NewTable(ctx *pulumi.Context, name string, args *TableArgs, opts ...pulumi.ResourceOption) (*Table, error) {
	if args == nil {
		args = &TableArgs{}
	}

	component := &Table{}
	err := ctx.RegisterComponentResource(tableIdentifier, name, component, opts...)
	if err != nil {
		return nil, err
	}

	opts = append(opts, pulumi.Parent(component))

	tableArgs := createTableArgs(args)

	table, err := dynamodb.NewTable(ctx, name, tableArgs, opts...)
	if err != nil {
		return nil, err
	}

	component.Outputs = table

	if err := ctx.RegisterResourceOutputs(component, pulumi.Map{
		"table": table,
	}); err != nil {
		return nil, err
	}

	return component, nil
}

func createTableArgs(args *TableArgs) *dynamodb.TableArgs {
	tableArgs := &dynamodb.TableArgs{}

	switch args.Type {
	case defaultTableType:
		hashKey := &dynamodb.TableAttributeArgs{
			Name: pulumi.String("id"),
			Type: pulumi.String("S"),
		}

		tableArgs.HashKey = pulumi.String("id")
		tableArgs.Attributes = dynamodb.TableAttributeArray{
			hashKey,
		}

		tableArgs.BillingMode = pulumi.String("PAY_PER_REQUEST")
	case basicTableType:
		tableArgs = args.Basic.ToTableArgs(tableArgs)
	case advancedTableType:
		tableArgs = args.Advanced.ToTableArgs(tableArgs)
	case expertTableType:
		tableArgs = args.Expert.ToTableArgs(tableArgs)
	}

	return tableArgs
}
