import socket
from server import server
from client import client
from utils import generate_password

def main():
    print("Welcome to remote desktop software")
    print("---------")
    print("Choose an option:")
    print("1. Remote a computer")
    print("2. Generate the IP and Password to others.")
    print("---------")
    choice = int(input("Your choice: "))
    print("---------")


    if choice == 1:
        ip = input("IP address: ")
        try:
            port = int(input("Port: "))            
            password = input("Password: ")
            client.start_client(ip, port, password)
        except:
            print("Invalid input!")
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
