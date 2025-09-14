import socket
import time
from itertools import permutations
import subprocess
from pprint import pprint

host = "10.10.131.116" #change this
knocked_ports = [1111, 2222, 3333, 4444]
tested_ports = [21, 22, 2375, 4420, 8080]


def nmap_scan(host, tested_ports):
    ports = ",".join(str(i) for i in tested_ports)
    result = subprocess.run(["nmap", "-sS", "-n", host, "-p", ports], capture_output=True, text=True)
    return result

def knocking(host, tested_ports,knocked_ports):
    result = nmap_scan(host, tested_ports)

    all_permutations = permutations(knocked_ports, 4)

    for sequence in all_permutations:

        for port in sequence:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            try:
                s.connect((host, port))
            except:
                pass    
            finally:
                s.close
                time.sleep(0.1)

        output = nmap_scan(host, tested_ports)
        if output.stdout != result.stdout:
            pprint({"sequence": sequence, "nmap_output": output.stdout})
            break

knocking(host, tested_ports, knocked_ports)