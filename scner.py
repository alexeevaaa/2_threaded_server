import socket

from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm


def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            return port
        else:
            return None
    except Exception as e:
        return None


    finally:
             sock.close()
        sock.close()


def scan_ports(host):
