from scapy.all import DNS, sniff

def filter_dns(packet):
    return DNS in packet

packets = sniff(timeout=10, lfilter=filter_dns)

# run in terminal: dig http://google.com

packets.show()

