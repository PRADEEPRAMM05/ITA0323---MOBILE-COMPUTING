"""Experiment 18: Call Blocking Probability Using the Erlang B Formula"""
import os

# INPUT
traffic_A = [5, 10, 15, 20]
channels_N = [5, 10, 15, 20, 25]
gos_targets = [0.01, 0.02, 0.05]
design_traffic = [10, 20, 40]

def erlang_b(A, N):
    """Erlang B via stable recursion B(0)=1, B(k)=A*B(k-1)/(k + A*B(k-1))"""
    B = 1.0
    for k in range(1, N + 1):
        B = A * B / (k + A * B)
    return B

def channels_needed(A, gos):
    N = 1
    while erlang_b(A, N) > gos:
        N += 1
    return N

print("=== INPUT ===")
print(f"Offered traffic A (Erlangs) : {traffic_A}")
print(f"Number of channels N        : {channels_N}")
print(f"GOS targets                 : {gos_targets}")
print(f"Dimensioning traffic (E)    : {design_traffic}")

print("\n=== OUTPUT ===")
print("Blocking probability Pb (rows: A in Erlangs, columns: N channels)")
print(f"{'A \\\\ N':>7}" + "".join(f"{n:>10}" for n in channels_N))
print("-" * (7 + 10 * len(channels_N)))
for A in traffic_A:
    print(f"{A:>7}" + "".join(f"{erlang_b(A, n):>10.4f}" for n in channels_N))

print("\nChannels required for a given GOS")
print(f"{'A (E)':>7}" + "".join(f"{'GOS=' + str(g):>12}" for g in gos_targets))
print("-" * (7 + 12 * len(gos_targets)))
for A in design_traffic:
    print(f"{A:>7}" + "".join(f"{channels_needed(A, g):>12}" for g in gos_targets))
