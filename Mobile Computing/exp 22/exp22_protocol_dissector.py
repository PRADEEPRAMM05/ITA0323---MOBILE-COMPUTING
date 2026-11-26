"""Experiment 22: Cellular Protocol Stack Packet Dissection (GSM / GTP-U / S1AP / NGAP)"""
import struct

PACKETS = [
    {
        "frame": 2345, "time": 12.345678, "src": "10.0.0.1", "dst": "10.0.0.2",
        "proto": "GTP-U", "info": "GTP-U, T-PDU (0xff), TEID: 0x12345678, Seq: 0x0001",
        "raw_hex": "30ff00201234567800010000"
    },
    {
        "frame": 2346, "time": 12.345679, "src": "10.0.0.2", "dst": "10.0.0.1",
        "proto": "S1AP", "info": "S1AP, Initial UE Message, eNB-UE-S1AP-ID: 104, TAC: 0x0001",
        "raw_hex": "000c001e000002000800020068001a000742f4100001"
    },
    {
        "frame": 2347, "time": 12.345680, "src": "10.0.0.1", "dst": "10.0.0.3",
        "proto": "NGAP", "info": "NGAP, Initial UE Message (5G Core), RAN-UE-NGAP-ID: 501",
        "raw_hex": "000f00220000030055000201f50026000602f8590001"
    }
]

def dissect_gtp(raw_hex):
    data = bytes.fromhex(raw_hex)
    flags, msg_type, length, teid = struct.unpack("!BBHI", data[:8])
    seq = struct.unpack("!H", data[8:10])[0] if len(data) >= 10 else 0
    return {
        "Flags": hex(flags),
        "Version": (flags >> 5) & 0x07,
        "Message Type": f"T-PDU ({hex(msg_type)})",
        "Length": length,
        "TEID": hex(teid),
        "Sequence Number": hex(seq)
    }

print("=== CELLULAR PROTOCOL STACK PACKET TRACE (Wireshark Capture) ===")
print(f"{'No.':<6} {'Time (s)':<12} {'Source':<12} {'Destination':<14} {'Protocol':<10} {'Information'}")
print("-" * 80)
for pkt in PACKETS:
    print(f"{pkt['frame']:<6} {pkt['time']:<12.6f} {pkt['src']:<12} {pkt['dst']:<14} {pkt['proto']:<10} {pkt['info']}")

print("\n=== PACKET DISSECTION TREE (GTP-U Frame 2345) ===")
gtp_fields = dissect_gtp(PACKETS[0]["raw_hex"])
for k, v in gtp_fields.items():
    print(f"  ▸ {k:<18}: {v}")
print(f"  ▸ Raw Byte Stream   : {' '.join(PACKETS[0]['raw_hex'][i:i+2] for i in range(0, len(PACKETS[0]['raw_hex']), 2))}")
