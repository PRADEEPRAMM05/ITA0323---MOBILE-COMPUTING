"""Experiment 26: Cellular Dynamic Network Performance Evaluation"""

time_s = [0, 25, 50, 75, 100, 125, 150, 175, 200]
throughput_mbps = [0.85, 0.88, 0.84, 0.80, 0.72, 0.85, 0.89, 0.90, 0.88]
pdr = [0.98, 0.99, 0.97, 0.95, 0.88, 0.98, 0.99, 0.99, 0.98]
delay_ms = [18.2, 18.0, 19.5, 22.0, 38.5, 19.0, 17.5, 17.2, 17.8]
packet_loss_pct = [2.0, 1.0, 3.0, 5.0, 12.0, 2.0, 1.0, 1.0, 2.0]

print("=== CELLULAR NETWORK DYNAMIC PERFORMANCE TELEMETRY ===")
print("Observation Period: 200 s | Cell Load Surge simulated at t = 100 s\n")
print(f"{'Time (s)':<10} {'Throughput (Mbps)':<20} {'PDR':<10} {'Delay (ms)':<15} {'Packet Loss (%)'}")
print("-" * 70)
for t, th, p, d, l in zip(time_s, throughput_mbps, pdr, delay_ms, packet_loss_pct):
    print(f"{t:<10} {th:<20.2f} {p:<10.2f} {d:<15.1f} {l:.1f}%")

print("-" * 70)
print(f"Average Throughput : {sum(throughput_mbps)/len(throughput_mbps):.2f} Mbps")
print(f"Average PDR        : {sum(pdr)/len(pdr)*100:.1f}%")
print(f"Average Delay      : {sum(delay_ms)/len(delay_ms):.1f} ms")
