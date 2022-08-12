// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export * from "./ipvs";
export * from "./provider";
export * from "./random";

// Export sub-modules:
import * as ipvs from "./ipvs";
import * as types from "./types";

export {
    ipvs,
    types,
};

// Import resources to register:
import { Ipvs } from "./ipvs";
import { Random } from "./random";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "linux:index:Ipvs":
                return new Ipvs(name, <any>undefined, { urn })
            case "linux:index:Random":
                return new Random(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("linux", "index", _module)

import { Provider } from "./provider";

pulumi.runtime.registerResourcePackage("linux", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:linux") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
