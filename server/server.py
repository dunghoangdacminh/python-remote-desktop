import signal
import socket
import threading

def signal_handler(sig, frame):
    print("\nTerminating the server...")
    exit(0)

def handle_client(client_socket, valid_password):
    while True:
        try:
            password = client_socket.recv(1024).decode('utf-8')
            if password == valid_password:
                client_socket.send("Connected successfully".encode('utf-8'))
                while True:
                    message = client_socket.recv(1024).decode('utf-8')
                    if message:
                        print(f"Received: {message}")
                        client_socket.send(f"Echo: {message}".encode('utf-8'))
                    else:
                        break
            else:
                client_socket.send("Invalid password".encode('utf-8'))
                break
        except:
            break
    client_socket.close()

def start_server(ip, port, valid_password):
    signal.signal(signal.SIGINT, signal_handler)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print(f"Server listening on {ip}:{port}")
    print("Press Control + C to terminate.")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, valid_password))
        client_handler.start()

if __name__ == "__main__":
    start_server('0.0.0.0', 9999, "valid_password")
