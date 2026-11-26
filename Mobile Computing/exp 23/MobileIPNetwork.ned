// MobileIPNetwork.ned - OMNeT++ INET Network Topology
package mobilecomputing.exp23;

import inet.node.inet.StandardHost;
import inet.node.inet.Router;
import inet.node.wireless.AccessPoint;
import inet.physicallayer.wireless.common.medium.RadioMedium;

network MobileIPNetwork
{
    parameters:
        @display("bgb=650,450;bgl=2");
    submodules:
        radioMedium: RadioMedium {
            @display("p=50,50");
        }
        homeAgent: StandardHost {
            @display("p=150,120;i=device/server");
        }
        foreignAgent: StandardHost {
            @display("p=480,120;i=device/server");
        }
        correspondentNode: StandardHost {
            @display("p=315,50;i=device/laptop");
        }
        mobileNode: StandardHost {
            @display("p=150,280;i=device/cellphone");
        }
        gatewayRouter: Router {
            @display("p=315,180");
        }
    connections:
        homeAgent.ethg++ <--> gatewayRouter.ethg++;
        foreignAgent.ethg++ <--> gatewayRouter.ethg++;
        correspondentNode.ethg++ <--> gatewayRouter.ethg++;
}
