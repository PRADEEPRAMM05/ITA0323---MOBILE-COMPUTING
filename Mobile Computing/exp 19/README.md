# Experiment 19: Mobile Cellular Handoff Simulation with Hysteresis

## 🎯 Aim & Objective
To simulate and evaluate mobile station handoff (handover) dynamics between two co-channel base stations separated by $D = 2000\text{ m}$ under log-normal correlated shadowing, and to demonstrate how an adaptive hysteresis margin $\Delta_h$ prevents the destructive "ping-pong" effect.

---

## 📐 Mathematical Formulation
1. **Distance-Dependent Path Loss Model:**
   $$P_{\text{loss}}(d) = P_{\text{ref}} - 10n\log_{10}\left(\frac{d}{d_0}\right)$$
2. **Gudmundson Correlated Log-Normal Shadowing (AR-1 Process):**
   $$S[k] = \rho \cdot S[k-1] + \sqrt{1 - \rho^2} \cdot W[k], \quad \rho = e^{-\frac{\Delta x}{d_{\text{corr}}}}, \quad W[k] \sim \mathcal{N}(0, \sigma^2)$$
3. **Hysteresis Decision Rule:**
   $$\text{Trigger Handoff from } \text{BS}_1 \to \text{BS}_2 \iff \text{RSS}_2(x) > \text{RSS}_1(x) + \Delta_h$$

---

## 💻 Simulation Implementation
- **Source Script:** [`exp19_handoff.py`](exp19_handoff.py)
- **Input Parameters:**
  - Base Station Distance $D = 2000\text{ m}$
  - Path Loss Exponent $n = 3.5$
  - Shadowing $\sigma = 4.0\text{ dB}$, Decorrelation Distance $d_{\text{corr}} = 50\text{ m}$
  - Step Size $\Delta x = 5\text{ m}$
  - Hysteresis Sweep: $\Delta_h \in [0, 3, 6, 9]\text{ dB}$

---

## 📊 Empirical Simulation Results

| Hysteresis Margin $\Delta_h$ (dB) | Total Handoff Count | Ping-Pong Suppression | Call Dropping Risk |
| :-: | :-: | :--- | :--- |
| **0 dB (No Margin)** | **11** | Extreme ping-pong fluctuations | High signaling overhead |
| **3 dB** | **3** | Moderate suppression | Balanced |
| **6 dB (Optimal)** | **1** | **Complete ping-pong elimination** | Low signaling load |
| **9 dB** | **1** | Stable handover | Late handoff / drag out |

---

## 🖼️ Execution Artifacts
![Experiment 19 Execution](Preview.png)
