import signal
import socket

def signal_handler(sig, frame):
    print("\nTerminating the program...")
    exit(0)

def start_client(ip, port, password):
    signal.signal(signal.SIGINT, signal_handler)
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        print("Connected to server")
        client.send(password.encode('utf-8'))

        while True:
            response = client.recv(1024).decode('utf-8')
            if response == "Invalid password":
                print("Invalid password. Connection closed.")
                break
            print(f"Server: {response}")

            message = input("Enter message: ")
            client.send(message.encode('utf-8'))
    except ConnectionRefusedError:
        print("Failed to connect to server. Please check the IP and port.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    ip = input("IP address: ")
    port = int(input("Port: "))
    password = input("Password: ")
    start_client(ip, port, password)
