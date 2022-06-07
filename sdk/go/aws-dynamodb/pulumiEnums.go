// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package awsdynamodb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The type of key for your DynamoDB Table.
type TableKeyType string

const (
	TableKeyTypeString = TableKeyType("string")
	TableKeyTypeNumber = TableKeyType("number")
)

// The type of DynamoDB Table.
type TableType string

const (
	TableTypeDefault  = TableType("default")
	TableTypeBasic    = TableType("basic")
	TableTypeAdvanced = TableType("advanced")
	TableTypeExpert   = TableType("expert")
)

func (TableType) ElementType() reflect.Type {
	return reflect.TypeOf((*TableType)(nil)).Elem()
}

func (e TableType) ToTableTypeOutput() TableTypeOutput {
	return pulumi.ToOutput(e).(TableTypeOutput)
}

func (e TableType) ToTableTypeOutputWithContext(ctx context.Context) TableTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(TableTypeOutput)
}

func (e TableType) ToTableTypePtrOutput() TableTypePtrOutput {
	return e.ToTableTypePtrOutputWithContext(context.Background())
}

func (e TableType) ToTableTypePtrOutputWithContext(ctx context.Context) TableTypePtrOutput {
	return TableType(e).ToTableTypeOutputWithContext(ctx).ToTableTypePtrOutputWithContext(ctx)
}

func (e TableType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e TableType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e TableType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e TableType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type TableTypeOutput struct{ *pulumi.OutputState }

func (TableTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TableType)(nil)).Elem()
}

func (o TableTypeOutput) ToTableTypeOutput() TableTypeOutput {
	return o
}

func (o TableTypeOutput) ToTableTypeOutputWithContext(ctx context.Context) TableTypeOutput {
	return o
}

func (o TableTypeOutput) ToTableTypePtrOutput() TableTypePtrOutput {
	return o.ToTableTypePtrOutputWithContext(context.Background())
}

func (o TableTypeOutput) ToTableTypePtrOutputWithContext(ctx context.Context) TableTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v TableType) *TableType {
		return &v
	}).(TableTypePtrOutput)
}

func (o TableTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o TableTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e TableType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o TableTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o TableTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e TableType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type TableTypePtrOutput struct{ *pulumi.OutputState }

func (TableTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TableType)(nil)).Elem()
}

func (o TableTypePtrOutput) ToTableTypePtrOutput() TableTypePtrOutput {
	return o
}

func (o TableTypePtrOutput) ToTableTypePtrOutputWithContext(ctx context.Context) TableTypePtrOutput {
	return o
}

func (o TableTypePtrOutput) Elem() TableTypeOutput {
	return o.ApplyT(func(v *TableType) TableType {
		if v != nil {
			return *v
		}
		var ret TableType
		return ret
	}).(TableTypeOutput)
}

func (o TableTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o TableTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *TableType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// TableTypeInput is an input type that accepts TableTypeArgs and TableTypeOutput values.
// You can construct a concrete instance of `TableTypeInput` via:
//
//          TableTypeArgs{...}
type TableTypeInput interface {
	pulumi.Input

	ToTableTypeOutput() TableTypeOutput
	ToTableTypeOutputWithContext(context.Context) TableTypeOutput
}

var tableTypePtrType = reflect.TypeOf((**TableType)(nil)).Elem()

type TableTypePtrInput interface {
	pulumi.Input

	ToTableTypePtrOutput() TableTypePtrOutput
	ToTableTypePtrOutputWithContext(context.Context) TableTypePtrOutput
}

type tableTypePtr string

func TableTypePtr(v string) TableTypePtrInput {
	return (*tableTypePtr)(&v)
}

func (*tableTypePtr) ElementType() reflect.Type {
	return tableTypePtrType
}

func (in *tableTypePtr) ToTableTypePtrOutput() TableTypePtrOutput {
	return pulumi.ToOutput(in).(TableTypePtrOutput)
}

func (in *tableTypePtr) ToTableTypePtrOutputWithContext(ctx context.Context) TableTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(TableTypePtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TableTypeInput)(nil)).Elem(), TableType("default"))
	pulumi.RegisterInputType(reflect.TypeOf((*TableTypePtrInput)(nil)).Elem(), TableType("default"))
	pulumi.RegisterOutputType(TableTypeOutput{})
	pulumi.RegisterOutputType(TableTypePtrOutput{})
}