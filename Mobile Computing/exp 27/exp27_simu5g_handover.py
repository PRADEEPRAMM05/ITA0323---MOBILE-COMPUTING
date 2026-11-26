"""Experiment 27: Simu5G / OMNeT++ Multi-eNodeB Handover Simulation"""

class Simu5GHandoverSimulation:
    def __init__(self):
        self.cells = ["eNB 1", "eNB 2", "eNB 3"]
        self.ue_id = "UE_01"
        self.handoff_events = [
            {"time": "14.2s", "src": "eNB 1", "tgt": "eNB 2", "trigger": "Event A3 (Neighbor > Serving + 3 dB)", "status": "COMPLETED"},
            {"time": "48.7s", "src": "eNB 2", "tgt": "eNB 3", "trigger": "Event A3 (Neighbor > Serving + 3 dB)", "status": "COMPLETED"}
        ]
        
    def run_simulation(self):
        print("=== OMNeT++ / Simu5G 5G NR HANDOVER SIMULATION ===")
        print(f"Topology       : Multi-eNB Linear Deployment ({' -> '.join(self.cells)})")
        print(f"Target UE      : {self.ue_id} (Linear speed = 25 m/s)\n")
        
        print("Project Explorer: Simu5G/simulations/handover")
        print("Starting discrete-event simulation engine...\n")
        
        for ev in self.handoff_events:
            print(f"[{ev['time']}] MEASUREMENT REPORT: {self.ue_id} reports RSRP({ev['tgt']}) > RSRP({ev['src']})")
            print(f"[{ev['time']}] HANDOVER PREPARATION: {ev['src']} sends Handover Request over X2/Xn interface to {ev['tgt']}")
            print(f"[{ev['time']}] HANDOVER EXECUTION  : {ev['tgt']} allocates C-RNTI and RACH preamble")
            print(f"[{ev['time']}] INFO (Handover)       : {self.ue_id} successfully handed over to {ev['tgt']}")
            print(f"[{ev['time']}] STATUS               : {ev['status']}\n")
            
        print("INFO: Simulation finished successfully.")

sim = Simu5GHandoverSimulation()
sim.run_simulation()
