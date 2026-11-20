# ITA0323 – Mobile Computing: Course Assignments & Laboratory Repository

**Student / GitHub User:** [PRADEEPRAMM05](https://github.com/PRADEEPRAMM05)  
**Repository:** [ITA0323---MOBILE-COMPUTING](https://github.com/PRADEEPRAMM05/ITA0323---MOBILE-COMPUTING)  
**Course Code:** ITA0323 – Mobile Computing  
**Environment:** Python 3.10+ / Java (OpenJDK 17+)  
**Execution:** Zero external runtime dependencies required (standard library compliant).

---

## 📚 Course Outcomes & Assignments Overview

This repository houses the complete theoretical derivations, architecture blueprints, performance evaluations, and simulation suites covering all five Course Outcomes (CO1 through CO5) of **ITA0323 - Mobile Computing**.

| Assignment Folder | Course Outcome | Core Topics & Focus | Total Tasks |
| :--- | :--- | :--- | :--- |
| **[Assignment 1/](Assignment%201/)** | **CO1** | **Hexagonal Cellular Network Design & Interference Management**: Spatial tessellation ($N = i^2 + ij + j^2$), reuse distance $D = R\sqrt{3N}$, $120^\circ$ directional sectoring, Erlang-B capacity planning, recursive cell splitting ($R \to R/2$, $P \to P/2^n$), Monte-Carlo SIR simulator, and 25k attendee stadium surge adaptation. | 12 Tasks |
| **[Assignment 2/](Assignment%202/)** | **CO2** | **Multiple Access Techniques & Physical Layer Engineering**: Mobile Communication vs Mobile Computing field audit, FDMA vs TDMA queueing under bursty IoT traffic, DS-CDMA Walsh-Hadamard code spreading and Near-Far closed-loop power control, OFDMA proportional fair subcarrier scheduling, and SDMA phased array beamforming. | 7 Tasks |
| **[Assignment 3/](Assignment%203/)** | **CO3** | **Wireless Networks, Mobility Management & Routing Protocols**: 802.11 Infrastructure vs IBSS (Ad-Hoc), CSMA/CA with RTS/CTS, Mobile IP (HA, FA, CoA, triangular routing vs route optimization, reverse tunneling), Cellular IP micro-mobility, DSDV loop-free proactive routing, and reactive AODV/DSR simulation. | 7 Tasks |
| **[Assignment 4/](Assignment%204/)** | **CO4** | **Mobile Application Environments & OS Architecture**: Multi-layered MobileOS repair (Kernel, HAL, Native Libs, ART, Framework), architectural comparison of Android vs iOS vs Windows, Dalvik vs ART runtime analysis (AOT/JIT, compacting GC), mobile security forensics, and power management (Doze Mode, App Standby). | 6 Tasks |
| **[Assignment 5/](Assignment%205/)** | **CO5** | **Android Features, Background Services & Performance Engineering**: Constraint-aware service orchestration (Foreground Services vs WorkManager), UI thread single-thread rule & ANR prevention, Offline-First Repository pattern, computation offloading energy trade-off model, working Java background suite, and 60/120 fps graphics budgeting. | 9 Tasks |
| **[Mobile Computing/](Mobile%20Computing/)** | **Lab Practical** | **Laboratory Experiments 01 to 10**: End-to-end user interfaces, architectural diagrams, call routing flows, handoff captures, and protocol stack previews. | 10 Experiments |

---

## 📁 Repository Directory Structure

```text
ITA0323---MOBILE-COMPUTING/
├── README.md
├── .gitignore
├── Assignment 1/                             # CO1: Cellular Network Planning (Tasks 01 to 12)
│   ├── README.md
│   ├── Task01/ (Frequency Planning Strategies, Pseudocode & Algorithms)
│   ├── Task02/ (Governing Parameters N, Q, R & Dynamic Scaling)
│   ├── Task03/ (Mathematical Derivations: Hex Geometry, SIR, Erlang-B)
│   ├── Task04/ (Best, Average, Worst-Case Boundary SIR & Traffic Dynamics)
│   ├── Task05/ (Scaling Laws 1/R², N^(n/2) & Break-Even Analysis)
│   ├── Task06/ (Cell Splitting Recurrence Formulation M_k = 4M_k-1)
│   ├── Task07/ (Closed-Form Solution k = ceil(log4(D/C0)) & Handoff Growth)
│   ├── Task08/ (cellular_planner.py: Python Hex Grid & Monte-Carlo Engine)
│   ├── Task09/ (Empirical Simulation Tables, SIR CDFs & Outage Data)
│   ├── Task10/ (Theory vs Simulation Gap Analysis & Trunking Penalties)
│   ├── Task11/ (Final Township HetNet Deployment Recommendation)
│   └── Task12/ (Day-4 Stadium Challenge: 25k Attendee COW/Wi-Fi Overlay)
│
├── Assignment 2/                             # CO2: Multiple Access Schemes (Tasks 01 to 07)
│   ├── README.md
│   ├── Task01/ (Mobile Comm vs Mobile Computing Technology Audit)
│   ├── Task02/ (FDMA vs TDMA Queueing & fdma_tdma_sim.py)
│   ├── Task03/ (CDMA Walsh Codes, Near-Far Problem & cdma_simulation.py)
│   ├── Task04/ (OFDMA Proportional Fair Allocation & ofdma_scheduler.py)
│   ├── Task05/ (SDMA Phased Array Beamforming & sdma_beamforming.py)
│   ├── Task06/ (Deployment Matrix: IoT, High-Speed Rail, Stadium, Rural)
│   └── Task07/ (Day-4 Redesign: Hybrid SC-FDMA / OFDMA Dual-Tier Scheduler)
│
├── Assignment 3/                             # CO3: Wireless Networks & Mobility (Tasks 01 to 07)
│   ├── README.md
│   ├── Task01/ (802.11 BSS/IBSS, Hidden Terminal & wifi_mac_sim.py)
│   ├── Task02/ (Mobile IP Mechanics, Triangular Routing & mobile_ip_sim.py)
│   ├── Task03/ (Cellular Infrastructure vs Ad-Hoc MANET Comparison Matrix)
│   ├── Task04/ (Micro-Mobility: Cellular IP & HAWAII Handoff Management)
│   ├── Task05/ (Proactive DSDV Sequence Numbers & dsdv_routing.py)
│   ├── Task06/ (Reactive AODV vs DSR Routing & manet_routing_sim.py)
│   └── Task07/ (Disaster Emergency Mesh Communication Blueprint)
│
├── Assignment 4/                             # CO4: Mobile Application OS Architecture (Tasks 01 to 06)
│   ├── README.md
│   ├── Task01/ (MobileOS Architecture Forensics & Corrected Multi-Layered Model)
│   ├── Task02/ (In-Depth OS Comparison: Android vs iOS vs Windows)
│   ├── Task03/ (Runtime Evolution: DVM vs ART & MemoryCompilationBenchmark.java)
│   ├── Task04/ (Mobile Security Forensics: Intent Hijacking & UID Sandboxing)
│   ├── Task05/ (Power Management: Doze Mode, App Standby, WakeLocks)
│   └── Task06/ (Day-4 Mission-Critical Field Operations Blueprint)
│
├── Assignment 5/                             # CO5: Android Features & Performance (Tasks A1 to B4)
│   ├── README.md
│   ├── TaskA1/ (Constraint-Aware Service & WorkManager Decision Tree)
│   ├── TaskA2/ (Concurrency Safety, Handler/Looper & ANR Prevention)
│   ├── TaskA3/ (Mobile Background Patterns: Offline-First Repository)
│   ├── TaskA4/ (Computation Offloading Energy Trade-off Model)
│   ├── TaskA5/ (Approximate Optimization: GPS Throttling & Batching)
│   ├── TaskB1/ (Java Background Suite: DataSyncWorker, LocationService, OfflineRepo)
│   ├── TaskB2/ (Adversarial Load Simulator: Network Flapping Stress Harness)
│   ├── TaskB3/ (UI / Graphics 60/120 FPS Budgeting & Overdraw Elimination)
│   └── TaskB4/ (Production Architecture Sign-Off & Telemetry Specification)
│
└── Mobile Computing/                         # Laboratory Experiments 01 to 10
    ├── exp 1/ (Evolution of Cellular Systems - Screenshots & Previews)
    ├── exp 2/ (Mobile Application UI & Workflow)
    ├── exp 3/ (GSM Network Switching Subsystem NSS)
    ├── exp 4/ (Wireless Protocol Stack)
    ├── exp 5/ (Location-Based Services LBS)
    ├── exp 6/ (Cellular Handoff / Handover Mechanism)
    ├── exp 7/ (Network Performance & Signal Quality Monitoring)
    ├── exp 8/ (Public Land Mobile Network PLMN & Roaming)
    ├── exp 9/ (GSM Security & Cell Architecture)
    └── exp 10/ (Multiple Access Techniques)
```

---

## 🚀 Execution & Verification Guide

All simulation engines and source code files are self-contained and run directly with standard Python 3 and Java:

### 1. Cellular Network Planner (Assignment 1)
```bash
python3 "Assignment 1/Task08/cellular_planner.py"
```

### 2. Multiple Access Simulators (Assignment 2)
```bash
python3 "Assignment 2/Task02/fdma_tdma_sim.py"
python3 "Assignment 2/Task03/cdma_simulation.py"
python3 "Assignment 2/Task04/ofdma_scheduler.py"
python3 "Assignment 2/Task05/sdma_beamforming.py"
```

### 3. Wireless Networks & Routing Protocols (Assignment 3)
```bash
python3 "Assignment 3/Task01/wifi_mac_sim.py"
python3 "Assignment 3/Task02/mobile_ip_sim.py"
python3 "Assignment 3/Task05/dsdv_routing.py"
python3 "Assignment 3/Task06/manet_routing_sim.py"
```

### 4. Mobile Runtime & Memory Benchmark (Assignment 4)
```bash
cd "Assignment 4/Task03"
javac MemoryCompilationBenchmark.java && java MemoryCompilationBenchmark
```

### 5. Mobile Background Architecture & Stress Testing (Assignment 5)
```bash
cd "Assignment 5/TaskB1/src"
javac com/university/mobile/repository/OfflineRepository.java com/university/mobile/background/DataSyncWorker.java com/university/mobile/service/LocationTrackingService.java

cd "../../../Assignment 5/TaskB2"
javac -cp "../TaskB1/src" AdversarialLoadSimulator.java && java -cp ".:../TaskB1/src" com.university.mobile.test.AdversarialLoadSimulator
```

---

## 👤 Author & Academic Details

- **Student Name:** Pradeepram M
- **GitHub Profile:** [@PRADEEPRAMM05](https://github.com/PRADEEPRAMM05)
- **Course:** ITA0323 – Mobile Computing
- **Institution:** SIMATS Engineering
