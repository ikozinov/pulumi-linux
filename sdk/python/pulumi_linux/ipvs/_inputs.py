# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'BackendArgs',
]

@pulumi.input_type
class BackendArgs:
    def __init__(__self__, *,
                 host: pulumi.Input[str],
                 port: pulumi.Input[int],
                 forwarder: Optional[pulumi.Input[str]] = None,
                 lthreshold: Optional[pulumi.Input[int]] = None,
                 uthreshold: Optional[pulumi.Input[int]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        Real server that an associated request for service may be assigned to. The server-address is the host address of a real server, and may plus port. Host can be either a plain IP address or a hostname. Port can be either a plain port number or the service name of port. In the case of the masquerading method, the host address is usually an RFC 1918 private IP address, and the port can be different from that of the associated service. With the tunneling and direct routing methods, port must be equal to that of the service address. For normal services, the port specified in the service address will be used if port is not specified. For fwmark services, port may be omitted, in which case the destination port on the real server will be the destination port of the request sent to the virtual service.
        :param pulumi.Input[str] host: The host of the server-address. Host can be either a plain IP address or a hostname.
        :param pulumi.Input[int] port: The port of the server-address.
        :param pulumi.Input[str] forwarder: forwarder is one of the 'g','i','m'
                g - gatewaying. Use gatewaying (direct routing). This is the default.
                i - ipip. Use ipip encapsulation (tunneling).
               m - masquerading. Use masquerading (network access translation, or NAT).
               Note: Regardless of the packet-forwarding mechanism specified, real servers for addresses for which there are interfaces on the local node will be use the local forwarding method, then packets for the servers will be passed to upper layer on the local node. This cannot be specified by ipvsadm, rather it set by the kernel as real servers are added or modified.
        :param pulumi.Input[int] lthreshold: lthreshold is an integer specifying the lower connection threshold of a server. The valid values of lthreshold are 0 through to 65535. The default is 0, which means the lower connection threshold is not set. If lthreshold is set with other values, the server will receive new connections when the number of its connections drops below its lower connection threshold. If lthreshold is not set but uthreshold is set, the server will receive new connections when the number of its connections drops below three forth of its upper connection threshold.
        :param pulumi.Input[int] uthreshold: uthreshold is an integer specifying the upper connection threshold of a server. The valid values of uthreshold are 0 through to 65535. The default is 0, which means the upper connection threshold is not set. If uthreshold is set with other values, no new connections will be sent to the server when the number of its connections exceeds its upper connection threshold.
        :param pulumi.Input[int] weight: Weight is an integer specifying the capacity of a server relative to the others in the pool. The valid values of weight are 0 through to 65535. The default is 1. Quiescent servers are specified with a weight of zero. A quiescent server will receive no new jobs but still serve the existing jobs, for all scheduling algorithms distributed with the Linux Virtual Server. Setting a quiescent server may be useful if the server is overloaded or needs to be taken out of service for maintenance.
        """
        pulumi.set(__self__, "host", host)
        pulumi.set(__self__, "port", port)
        if forwarder is None:
            forwarder = 'g'
        if forwarder is not None:
            pulumi.set(__self__, "forwarder", forwarder)
        if lthreshold is not None:
            pulumi.set(__self__, "lthreshold", lthreshold)
        if uthreshold is not None:
            pulumi.set(__self__, "uthreshold", uthreshold)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def host(self) -> pulumi.Input[str]:
        """
        The host of the server-address. Host can be either a plain IP address or a hostname.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: pulumi.Input[str]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        """
        The port of the server-address.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def forwarder(self) -> Optional[pulumi.Input[str]]:
        """
        forwarder is one of the 'g','i','m'
         g - gatewaying. Use gatewaying (direct routing). This is the default.
         i - ipip. Use ipip encapsulation (tunneling).
        m - masquerading. Use masquerading (network access translation, or NAT).
        Note: Regardless of the packet-forwarding mechanism specified, real servers for addresses for which there are interfaces on the local node will be use the local forwarding method, then packets for the servers will be passed to upper layer on the local node. This cannot be specified by ipvsadm, rather it set by the kernel as real servers are added or modified.
        """
        return pulumi.get(self, "forwarder")

    @forwarder.setter
    def forwarder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "forwarder", value)

    @property
    @pulumi.getter
    def lthreshold(self) -> Optional[pulumi.Input[int]]:
        """
        lthreshold is an integer specifying the lower connection threshold of a server. The valid values of lthreshold are 0 through to 65535. The default is 0, which means the lower connection threshold is not set. If lthreshold is set with other values, the server will receive new connections when the number of its connections drops below its lower connection threshold. If lthreshold is not set but uthreshold is set, the server will receive new connections when the number of its connections drops below three forth of its upper connection threshold.
        """
        return pulumi.get(self, "lthreshold")

    @lthreshold.setter
    def lthreshold(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "lthreshold", value)

    @property
    @pulumi.getter
    def uthreshold(self) -> Optional[pulumi.Input[int]]:
        """
        uthreshold is an integer specifying the upper connection threshold of a server. The valid values of uthreshold are 0 through to 65535. The default is 0, which means the upper connection threshold is not set. If uthreshold is set with other values, no new connections will be sent to the server when the number of its connections exceeds its upper connection threshold.
        """
        return pulumi.get(self, "uthreshold")

    @uthreshold.setter
    def uthreshold(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "uthreshold", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        """
        Weight is an integer specifying the capacity of a server relative to the others in the pool. The valid values of weight are 0 through to 65535. The default is 1. Quiescent servers are specified with a weight of zero. A quiescent server will receive no new jobs but still serve the existing jobs, for all scheduling algorithms distributed with the Linux Virtual Server. Setting a quiescent server may be useful if the server is overloaded or needs to be taken out of service for maintenance.
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


