"""Experiment 23: Mobile IP Registration & Triangular Routing Simulator"""
import math

class MobileIPSimulator:
    def __init__(self):
        self.home_net = "192.168.1.0/24"
        self.foreign_net = "10.0.2.0/24"
        self.home_agent = "192.168.1.1"
        self.foreign_agent = "10.0.2.1"
        self.home_address = "192.168.1.100"
        self.care_of_address = "10.0.2.100"
        self.cn_address = "172.16.0.50"
        
    def simulate_mobility(self):
        print("=== STAGE 1: Mobile Node at Home Network ===")
        print(f"  MN IP        : {self.home_address}")
        print(f"  Location     : Home Subnet ({self.home_net})")
        print("  Route        : Standard direct IP routing (CN <---> MN)")
        
        print("\n=== STAGE 2: Movement to Foreign Network & Agent Discovery ===")
        print(f"  MN moves to  : Foreign Subnet ({self.foreign_net})")
        print(f"  FA Beaconing : Foreign Agent ({self.foreign_agent}) broadcasts Agent Advertisement")
        print(f"  CoA Assigned : {self.care_of_address} (Foreign Agent CoA)")
        
        print("\n=== STAGE 3: Registration Signaling ===")
        print(f"  1. MN -> FA  : Registration Request (HoA={self.home_address}, HA={self.home_agent}, CoA={self.care_of_address})")
        print(f"  2. FA -> HA  : Relays Registration Request across backbone")
        print(f"  3. HA Updates: Binding Cache -> [HoA: {self.home_address} | CoA: {self.care_of_address} | Lifetime: 1800s]")
        print(f"  4. HA -> FA  : Registration Reply (Status: 0x00 OK)")
        print(f"  5. FA -> MN  : Registration Success Confirmation")
        
        print("\n=== STAGE 4: Data Plane Tunneling (Triangular Routing) ===")
        print(f"  Forward Path : CN ({self.cn_address}) -> HA ({self.home_agent})")
        print(f"  Tunneling    : HA encapsulates original IP inside outer IP header: [{self.home_agent} -> {self.care_of_address}]")
        print(f"  Decapsulation: FA strips outer header, delivers inner datagram to MN ({self.home_address})")
        print(f"  Reverse Path : MN -> CN (Direct or Reverse Tunnel via HA)")

sim = MobileIPSimulator()
sim.simulate_mobility()
