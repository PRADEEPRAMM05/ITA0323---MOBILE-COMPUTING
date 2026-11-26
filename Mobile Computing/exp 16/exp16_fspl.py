"""Experiment 16: Free-Space Path Loss and Received Power"""
import os, math

# INPUT
Pt_dBm = 43.0                 # transmitter power (dBm), about 20 W
Gt_dBi = 12.0                 # transmit antenna gain (dBi)
Gr_dBi = 0.0                  # receive antenna gain (dBi)
freqs_MHz = [900, 1800, 2100, 2600]
table_dist_km = [0.1, 1, 5, 10]
rx_sensitivity_dBm = -100.0   # receiver sensitivity (dBm)

def fspl_db(d_km, f_mhz):
    """FSPL (dB) = 32.44 + 20 log10(d_km) + 20 log10(f_MHz)"""
    return 32.44 + 20 * math.log10(d_km) + 20 * math.log10(f_mhz)

def rx_power_dbm(d_km, f_mhz):
    """Pr(dBm) = Pt + Gt + Gr - FSPL"""
    return Pt_dBm + Gt_dBi + Gr_dBi - fspl_db(d_km, f_mhz)

def max_range_km(f_mhz):
    """Distance at which Pr equals the receiver sensitivity."""
    budget = Pt_dBm + Gt_dBi + Gr_dBi - rx_sensitivity_dBm
    return 10 ** ((budget - 32.44 - 20 * math.log10(f_mhz)) / 20)

print("=== INPUT ===")
print(f"Transmit power Pt        : {Pt_dBm} dBm")
print(f"Transmit antenna gain Gt : {Gt_dBi} dBi")
print(f"Receive antenna gain Gr  : {Gr_dBi} dBi")
print(f"Frequencies              : {freqs_MHz} MHz")
print(f"Distances                : {table_dist_km} km")
print(f"Receiver sensitivity     : {rx_sensitivity_dBm} dBm")

print("\n=== OUTPUT ===")
print(f"{'f (MHz)':>8} {'d (km)':>8} {'FSPL (dB)':>11} {'Pr (dBm)':>10}")
print("-" * 40)
for f in freqs_MHz:
    for d in table_dist_km:
        print(f"{f:>8} {d:>8} {fspl_db(d, f):>11.2f} {rx_power_dbm(d, f):>10.2f}")
print("-" * 40)
print("Maximum range for Pr >= sensitivity:")
for f in freqs_MHz:
    print(f"  f = {f:>4} MHz -> d_max = {max_range_km(f):8.2f} km")
