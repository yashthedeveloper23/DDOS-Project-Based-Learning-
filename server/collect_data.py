from scapy.all import sniff, wrpcap
import os

# Directory to save the captured packets
output_dir = '/workspaces/DDOS-Project-Based-Learning-/server/data'
os.makedirs(output_dir, exist_ok=True)

# Output file for captured packets
output_file = os.path.join(output_dir, 'captured_packets.pcap')

# Function to process each packet
def process_packet(packet):
    print(f"Packet captured: {packet.summary()}")

# Capture packets
def capture_packets(interface='eth0', packet_count=100):
    print(f"Starting packet capture on interface {interface}...")
    packets = sniff(iface=interface, count=packet_count, prn=process_packet)
    wrpcap(output_file, packets)
    print(f"Packet capture complete. {packet_count} packets saved to {output_file}")

if __name__ == "__main__":
    capture_packets()