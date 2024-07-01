import signal
import socket
from server import server
from client import client
from utils import generate_password

def signal_handler(sig, frame):
    print("\nTerminating the program...")
    exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    print("Welcome to remote desktop software")
    print("---------")
    print("Choose an option:")
    print("1. Remote a computer")
    print("2. Generate the IP and Password to others.")
    print("Press Control + C to terminate.")
    print("---------")
    choice = int(input("Your choice: "))
    print("---------")

    if choice == 1:
        ip = input("IP address: ")
        port = int(input("Port: "))
        password = input("Password: ")
        client.start_client(ip, port, password)
    elif choice == 2:
        ip = socket.gethostbyname(socket.gethostname())
        port = 9999
        password = generate_password.generate_password()
        print(f"Your IP: {ip}")
        print(f"Your Password: {password}")
        server.start_server(ip, port, password)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
