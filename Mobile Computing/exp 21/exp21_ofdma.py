"""Experiment 21: Effect of the OFDMA Downlink Scheduler on User Throughput and Fairness"""
import os, math, random

# INPUT
n_users = 6
n_rb = 25                     # resource blocks per TTI
n_tti = 3000                  # simulated sub-frames (1 ms each)
avg_snr_dB = [25, 20, 15, 10, 5, 0] # mean SNR of each user (near -> far)
rb_bw = 180e3                 # bandwidth of one resource block (Hz)
tti = 1e-3                    # TTI duration (s)
pf_window = 100               # PF averaging window (TTIs)

avg_snr = [10 ** (x / 10.0) for x in avg_snr_dB]

def jain(x):
    return (sum(x) ** 2) / (len(x) * sum(v * v for v in x))

random.seed(7)

def simulate(scheme):
    served_bits = [0.0] * n_users
    avg_rate = [1.0] * n_users
    random.seed(7)
    for t in range(n_tti):
        # Rayleigh channel rates
        rates = []
        for u in range(n_users):
            user_rates = []
            for rb in range(n_rb):
                gain = random.expovariate(1.0)
                snr = avg_snr[u] * gain
                r = rb_bw * math.log2(1.0 + snr)
                user_rates.append(r)
            rates.append(user_rates)
        
        got = [0.0] * n_users
        for rb in range(n_rb):
            if scheme == "Round Robin":
                chosen = (rb + t) % n_users
            elif scheme == "Max C/I":
                chosen = max(range(n_users), key=lambda u: rates[u][rb])
            else: # Proportional Fair
                chosen = max(range(n_users), key=lambda u: rates[u][rb] / avg_rate[u])
            got[chosen] += rates[chosen][rb]
        
        for u in range(n_users):
            served_bits[u] += got[u] * tti
            avg_rate[u] = (1.0 - 1.0 / pf_window) * avg_rate[u] + (1.0 / pf_window) * got[u]
            
    return [b / (n_tti * tti) / 1e6 for b in served_bits]

print("=== INPUT ===")
print(f"Users: {n_users}, resource blocks: {n_rb}, TTIs: {n_tti}")
print(f"Average SNR per user (dB): {avg_snr_dB}")
print(f"RB bandwidth: {rb_bw / 1e3:.0f} kHz, TTI: {tti * 1e3:.0f} ms, PF window: {pf_window} TTIs")
print("Channel: Rayleigh fading, independent per user, RB and TTI")

schemes = ["Round Robin", "Max C/I", "Proportional Fair"]
res = {s: simulate(s) for s in schemes}

print("\n=== OUTPUT ===")
print("Per-user throughput (Mbit/s)")
hdr = f"{'Scheduler':<19}" + "".join(f"{('U' + str(u + 1)):>7}" for u in range(n_users)) + f"{'Total':>8}{'Jain':>7}"
print(hdr)
print("-" * len(hdr))
for s in schemes:
    r = res[s]
    print(f"{s:<19}" + "".join(f"{v:>7.2f}" for v in r) + f"{sum(r):>8.2f}{jain(r):>7.3f}")
