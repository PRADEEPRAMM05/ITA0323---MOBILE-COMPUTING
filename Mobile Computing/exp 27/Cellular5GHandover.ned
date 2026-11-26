// Cellular5GHandover.ned - OMNeT++ Simu5G Multi-Cell Handover Topology
package mobilecomputing.exp27;

import simu5g.nodes.NR.gNodeB;
import simu5g.nodes.NR.NRUe;
import simu5g.common.carrierAggregation.CarrierAggregation;
import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;

network Cellular5GHandover
{
    parameters:
        @display("bgb=900,500;bgl=2");
    submodules:
        configurator: Ipv4NetworkConfigurator {
            @display("p=50,50");
        }
        eNB1: gNodeB {
            @display("p=180,220;i=device/antennatower");
        }
        eNB2: gNodeB {
            @display("p=450,220;i=device/antennatower");
        }
        eNB3: gNodeB {
            @display("p=720,220;i=device/antennatower");
        }
        ue: NRUe {
            @display("p=180,350;i=device/cellphone");
        }
}
