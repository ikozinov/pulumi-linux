// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Linux
{
    /// <summary>
    /// IPVS is used to set up, maintain or inspect the virtual server table in the Linux kernel. The Linux Virtual Server can be used to build scalable network services based on a cluster of two or more nodes. The active node of the cluster redirects service requests to a collection of server hosts that will actually perform the services. Supported features include two protocols (TCP and UDP), three packet-forwarding methods (NAT, tunneling, and direct routing), and eight load balancing algorithms (round robin, weighted round robin, least-connection, weighted least-connection, locality-based least-connection, locality-based least-connection with replication, destination-hashing, and source-hashing).
    /// The connection is established via ssh.
    /// </summary>
    [LinuxResourceType("linux:index:Ipvs")]
    public partial class Ipvs : global::Pulumi.ComponentResource
    {
        /// <summary>
        /// Create a Ipvs resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Ipvs(string name, IpvsArgs args, ComponentResourceOptions? options = null)
            : base("linux:index:Ipvs", name, args ?? new IpvsArgs(), MakeResourceOptions(options, ""), remote: true)
        {
        }

        private static ComponentResourceOptions MakeResourceOptions(ComponentResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new ComponentResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = ComponentResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class IpvsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Install ipvsadm and modules on target instance
        /// </summary>
        [Input("provision", required: true)]
        public Input<bool> Provision { get; set; } = null!;

        /// <summary>
        /// The parameters with which to connect to the remote host
        /// </summary>
        [Input("sshConnection", required: true)]
        public Input<Inputs.SshConnectionArgs> SshConnection { get; set; } = null!;

        public IpvsArgs()
        {
            Provision = true;
        }
        public static new IpvsArgs Empty => new IpvsArgs();
    }
}
