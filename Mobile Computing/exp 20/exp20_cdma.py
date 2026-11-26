"""Experiment 20: Direct-Sequence CDMA Spreading and Despreading with Walsh Codes"""
import os, math, random

# INPUT
L = 8                         # spreading factor (Walsh code length)
# 8x8 Hadamard matrix
H2 = [[1, 1], [1, -1]]
def make_hadamard(n):
    if n == 1:
        return [[1]]
    h_sub = make_hadamard(n // 2)
    top = [r + r for r in h_sub]
    bot = [r + [-x for x in r] for r in h_sub]
    return top + bot

H8 = make_hadamard(8)
codes = [H8[1], H8[2], H8[4]]
data = [
    [1, -1, 1, 1, -1],        # user 1 bits
    [-1, -1, 1, -1, 1],       # user 2 bits
    [1, 1, -1, 1, -1]         # user 3 bits
]
noise_sigma = 1.5
ber_sigmas = [0.5, 1.0, 2.0, 3.0, 4.0]

def spread(bits, code):
    out = []
    for b in bits:
        out.extend([b * c for c in code])
    return out

def despread(rx, code):
    bits = len(rx) // L
    corr = []
    rec = []
    for i in range(bits):
        chunk = rx[i*L : (i+1)*L]
        val = sum(x * c for x, c in zip(chunk, code)) / float(L)
        corr.append(round(val, 2))
        rec.append(1 if val >= 0 else -1)
    return corr, rec

print("=== INPUT ===")
print(f"Spreading factor L = {L} (processing gain = {10 * math.log10(L):.2f} dB)")
for u in range(3):
    print(f"User {u+1}: code = {codes[u]}")
    print(f"        data = {data[u]}")
print(f"AWGN sigma on chips = {noise_sigma}")

tx1 = spread(data[0], codes[0])
tx2 = spread(data[1], codes[1])
tx3 = spread(data[2], codes[2])
composite = [a + b + c for a, b, c in zip(tx1, tx2, tx3)]

random.seed(42)
noisy = [c + random.gauss(0, noise_sigma) for c in composite]

print("\n=== OUTPUT ===")
print("Code orthogonality check (dot product / L):")
for u in range(3):
    row = [sum(a * b for a, b in zip(codes[u], codes[v])) // L for v in range(3)]
    print(row)

print(f"\nComposite signal, first bit period: {composite[:L]}")
print("\nNoise-free despreading:")
for u in range(3):
    corr, rec = despread(composite, codes[u])
    print(f"  User {u+1}: correlator = {corr}")
    print(f"          recovered  = {rec}  match = {rec == data[u]}")

print(f"\nWith AWGN (sigma = {noise_sigma}):")
for u in range(3):
    corr, rec = despread(noisy, codes[u])
    errs = sum(1 for a, b in zip(rec, data[u]) if a != b)
    print(f"  User {u+1}: recovered  = {rec}  bit errors = {errs}")

unused = H8[5]
corr_unused, _ = despread(composite, unused)
print(f"\nCorrelating with an unassigned code (row 5): {corr_unused}")

print("\nBER of user 1 versus noise level (3 active users):")
print(f"{'sigma':>7} {'BER':>10}")
for s in ber_sigmas:
    n_bits = 2000
    b1 = [random.choice([-1, 1]) for _ in range(n_bits)]
    b2 = [random.choice([-1, 1]) for _ in range(n_bits)]
    b3 = [random.choice([-1, 1]) for _ in range(n_bits)]
    c1 = spread(b1, codes[0])
    c2 = spread(b2, codes[1])
    c3 = spread(b3, codes[2])
    comp = [x + y + z + random.gauss(0, s) for x, y, z in zip(c1, c2, c3)]
    _, rec1 = despread(comp, codes[0])
    ber = sum(1 for a, b in zip(rec1, b1) if a != b) / float(n_bits)
    print(f"{s:>7} {ber:>10.4f}")
