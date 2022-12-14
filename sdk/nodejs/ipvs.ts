// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * IPVS is used to set up, maintain or inspect the virtual server table in the Linux kernel. The Linux Virtual Server can be used to build scalable network services based on a cluster of two or more nodes. The active node of the cluster redirects service requests to a collection of server hosts that will actually perform the services. Supported features include two protocols (TCP and UDP), three packet-forwarding methods (NAT, tunneling, and direct routing), and eight load balancing algorithms (round robin, weighted round robin, least-connection, weighted least-connection, locality-based least-connection, locality-based least-connection with replication, destination-hashing, and source-hashing).
 * The connection is established via ssh.
 */
export class Ipvs extends pulumi.ComponentResource {
    /** @internal */
    public static readonly __pulumiType = 'linux:index:Ipvs';

    /**
     * Returns true if the given object is an instance of Ipvs.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Ipvs {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Ipvs.__pulumiType;
    }


    /**
     * Create a Ipvs resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IpvsArgs, opts?: pulumi.ComponentResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.provision === undefined) && !opts.urn) {
                throw new Error("Missing required property 'provision'");
            }
            if ((!args || args.sshConnection === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sshConnection'");
            }
            resourceInputs["provision"] = (args ? args.provision : undefined) ?? true;
            resourceInputs["sshConnection"] = args ? (args.sshConnection ? pulumi.output(args.sshConnection).apply(inputs.sshConnectionArgsProvideDefaults) : undefined) : undefined;
        } else {
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Ipvs.__pulumiType, name, resourceInputs, opts, true /*remote*/);
    }
}

/**
 * The set of arguments for constructing a Ipvs resource.
 */
export interface IpvsArgs {
    /**
     * Install ipvsadm and modules on target instance
     */
    provision: pulumi.Input<boolean>;
    /**
     * The parameters with which to connect to the remote host
     */
    sshConnection: pulumi.Input<inputs.SshConnectionArgs>;
}
