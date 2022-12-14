// Code generated by pulumigen DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package linux

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Instructions for how to connect to a remote endpoint.
type SshConnection struct {
	// The address of the resource to connect to.
	Host string `pulumi:"host"`
	// The password we should use for the connection.
	Password *string `pulumi:"password"`
	// The port to connect to.
	Port *float64 `pulumi:"port"`
	// The contents of an SSH key to use for the connection. This takes preference over the password if provided.
	PrivateKey *string `pulumi:"privateKey"`
	// The user that we should use for the connection.
	User *string `pulumi:"user"`
}

// Defaults sets the appropriate defaults for SshConnection
func (val *SshConnection) Defaults() *SshConnection {
	if val == nil {
		return nil
	}
	tmp := *val
	if isZero(tmp.Port) {
		port_ := 22.0
		tmp.Port = &port_
	}
	if isZero(tmp.User) {
		user_ := "root"
		tmp.User = &user_
	}
	return &tmp
}

// SshConnectionInput is an input type that accepts SshConnectionArgs and SshConnectionOutput values.
// You can construct a concrete instance of `SshConnectionInput` via:
//
//          SshConnectionArgs{...}
type SshConnectionInput interface {
	pulumi.Input

	ToSshConnectionOutput() SshConnectionOutput
	ToSshConnectionOutputWithContext(context.Context) SshConnectionOutput
}

// Instructions for how to connect to a remote endpoint.
type SshConnectionArgs struct {
	// The address of the resource to connect to.
	Host pulumi.StringInput `pulumi:"host"`
	// The password we should use for the connection.
	Password pulumi.StringPtrInput `pulumi:"password"`
	// The port to connect to.
	Port pulumi.Float64PtrInput `pulumi:"port"`
	// The contents of an SSH key to use for the connection. This takes preference over the password if provided.
	PrivateKey pulumi.StringPtrInput `pulumi:"privateKey"`
	// The user that we should use for the connection.
	User pulumi.StringPtrInput `pulumi:"user"`
}

// Defaults sets the appropriate defaults for SshConnectionArgs
func (val *SshConnectionArgs) Defaults() *SshConnectionArgs {
	if val == nil {
		return nil
	}
	tmp := *val
	if isZero(tmp.Port) {
		tmp.Port = pulumi.Float64Ptr(22.0)
	}
	if isZero(tmp.User) {
		tmp.User = pulumi.StringPtr("root")
	}
	return &tmp
}
func (SshConnectionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SshConnection)(nil)).Elem()
}

func (i SshConnectionArgs) ToSshConnectionOutput() SshConnectionOutput {
	return i.ToSshConnectionOutputWithContext(context.Background())
}

func (i SshConnectionArgs) ToSshConnectionOutputWithContext(ctx context.Context) SshConnectionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SshConnectionOutput)
}

// Instructions for how to connect to a remote endpoint.
type SshConnectionOutput struct{ *pulumi.OutputState }

func (SshConnectionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SshConnection)(nil)).Elem()
}

func (o SshConnectionOutput) ToSshConnectionOutput() SshConnectionOutput {
	return o
}

func (o SshConnectionOutput) ToSshConnectionOutputWithContext(ctx context.Context) SshConnectionOutput {
	return o
}

// The address of the resource to connect to.
func (o SshConnectionOutput) Host() pulumi.StringOutput {
	return o.ApplyT(func(v SshConnection) string { return v.Host }).(pulumi.StringOutput)
}

// The password we should use for the connection.
func (o SshConnectionOutput) Password() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SshConnection) *string { return v.Password }).(pulumi.StringPtrOutput)
}

// The port to connect to.
func (o SshConnectionOutput) Port() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v SshConnection) *float64 { return v.Port }).(pulumi.Float64PtrOutput)
}

// The contents of an SSH key to use for the connection. This takes preference over the password if provided.
func (o SshConnectionOutput) PrivateKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SshConnection) *string { return v.PrivateKey }).(pulumi.StringPtrOutput)
}

// The user that we should use for the connection.
func (o SshConnectionOutput) User() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SshConnection) *string { return v.User }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SshConnectionInput)(nil)).Elem(), SshConnectionArgs{})
	pulumi.RegisterOutputType(SshConnectionOutput{})
}
