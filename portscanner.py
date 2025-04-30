import socket

def scan_ports(ip, start_port, end_port):
    open_ports = []

    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)  # Set timeout for connection attempt
                result = sock.connect_ex((ip, port))  # 0 means open
                if result == 0:
                    open_ports.append(port)
        except socket.error:
            print(f"Couldn't connect to {ip}. Is the IP correct?")
            return []

    return open_ports


def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


if __name__ == "__main__":
    print("=== Basic Port Scanner ===")
    ip = input("Enter IP address to scan: ")

    if not is_valid_ip(ip):
        print("Invalid IP address format.")
        exit()

    try:
        start_port = int(input("Enter start port (0-65535): "))
        end_port = int(input("Enter end port (0-65535): "))

        if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535 and start_port <= end_port):
            raise ValueError

    except ValueError:
        print("Invalid port range. Please enter numbers between 0 and 65535.")
        exit()

    open_ports = scan_ports(ip, start_port, end_port)

    if open_ports:
        print(f"\nOpen ports on {ip}: {open_ports}")
    else:
        print(f"\nNo open ports found on {ip} in the given range.")
