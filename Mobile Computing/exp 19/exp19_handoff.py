"""Experiment 19: Handoff Simulation with Hysteresis"""
import os, math, random

# INPUT
D = 2000.0                   # distance between BS1 (x = 0) and BS2 (x = D), meters
step = 5.0                    # mobile position step (m)
P_ref = -30.0                 # received power at reference distance (dBm)
d0 = 10.0                     # reference distance (m)
n_exp = 3.5                   # path-loss exponent
sigma = 4.0                   # shadowing standard deviation (dB)
d_corr = 50.0                 # shadowing decorrelation distance (m)
hysteresis_dB = [0, 3, 6, 9]

random.seed(1)
x = [i * step for i in range(int(D / step) + 1)]
n_points = len(x)

def generate_shadowing(n):
    a = math.exp(-step / d_corr)
    s = [0.0] * n
    s[0] = random.gauss(0, sigma)
    for k in range(1, n):
        s[k] = a * s[k - 1] + math.sqrt(1 - a * a) * random.gauss(0, sigma)
    return s

def rss(dist):
    d = max(dist, d0)
    return P_ref - 10 * n_exp * math.log10(d / d0)

sh1 = generate_shadowing(n_points)
sh2 = generate_shadowing(n_points)
rss1 = [rss(dist) + s for dist, s in zip(x, sh1)]
rss2 = [rss(D - dist) + s for dist, s in zip(x, sh2)]

def simulate_handoff(delta_h):
    current_bs = 1
    handoffs = 0
    server = []
    for r1, r2 in zip(rss1, rss2):
        if current_bs == 1 and (r2 > r1 + delta_h):
            current_bs = 2
            handoffs += 1
        elif current_bs == 2 and (r1 > r2 + delta_h):
            current_bs = 1
            handoffs += 1
        server.append(current_bs)
    return handoffs, server

print("=== INPUT ===")
print(f"Base station separation D : {D} m")
print(f"Path loss exponent n      : {n_exp}")
print(f"Shadowing sigma           : {sigma} dB (decorrelation {d_corr} m)")
print(f"Hysteresis values Delta_h : {hysteresis_dB} dB")

print("\n=== OUTPUT ===")
print(f"{'Delta_h (dB)':>12} {'Handoff count':>15}")
print("-" * 30)
for h in hysteresis_dB:
    cnt, _ = simulate_handoff(h)
    print(f"{h:>12} {cnt:>15}")
