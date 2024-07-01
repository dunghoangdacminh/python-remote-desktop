import socket

def start_client(ip, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        print("Connected to server")

        while True:
            message = input("Enter message: ")
            client.send(message.encode('utf-8'))

            response = client.recv(1024).decode('utf-8')
            if response == "Invalid password":
                print("Invalid password. Connection closed.")
                break
            print(f"Server: {response}")
    except ConnectionRefusedError:
        print("Failed to connect to server. Please check the IP and port.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ip = input("IP address: ")
    port = int(input("Port: "))
    start_client(ip, port)
