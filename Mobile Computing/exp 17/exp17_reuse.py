"""Experiment 17: Frequency (Co-channel) Reuse - Cluster Size, Capacity and S/I"""
import os, math

S_total = 336                 # total duplex channels allocated to the system
M_cells = 84                  # total number of cells covering the service area
n_exp = 4                     # path-loss exponent
SIR_required_dB = 18.0        # required S/I (AMPS-type voice quality)
ij_pairs = [(1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (2, 2), (3, 1)]
N_INTERFERERS = 6             # first-tier co-channel cells (hexagonal layout)

print("=== INPUT ===")
print(f"Total channels S         : {S_total}")
print(f"Total cells in system M  : {M_cells}")
print(f"Path-loss exponent n     : {n_exp}")
print(f"Required S/I             : {SIR_required_dB} dB")
print(f"Shift parameters (i, j)  : {ij_pairs}")

print("\n=== OUTPUT ===")
hdr = f"{'i':>2} {'j':>2} {'N':>3} {'D/R':>6} {'k=S/N':>7} {'S/I (dB)':>9} {'Capacity C':>11} {'S/I ok?':>8}"
print(hdr)
print("-" * len(hdr))

Ns, sirs, caps = [], [], []
for i, j in ij_pairs:
    N = i * i + i * j + j * j
    q = math.sqrt(3 * N)
    k = S_total // N
    sir_linear = (q ** n_exp) / N_INTERFERERS
    sir_db = 10 * math.log10(sir_linear)
    C = (M_cells // N) * S_total
    ok = "YES" if sir_db >= SIR_required_dB else "NO"
    print(f"{i:>2} {j:>2} {N:>3} {q:>6.2f} {k:>7} {sir_db:>9.2f} {C:>11} {ok:>8}")
