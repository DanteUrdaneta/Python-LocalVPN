import socket 
import select
from modules.user import user_class
from modules.security_functions import validate_password


def create_server(server_address, server_port, password):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_address, server_port))
    server_socket.listen(1)
    client_sockets = [server_socket]
    print(f"Server listening on {server_address}:{server_port}")

    try:
        while True:
            readable, _, _ = select.select(client_sockets, [], [])
            for s in readable:
                if s == server_socket:
                    # Accept new connection
                    client_socket, client_address = server_socket.accept()
                    client_sockets.append(client_socket)
                    print(f"Client connected from {client_address[0]}:{client_address[1]}")
                    info = True

                    # Validate password
                    receive_password = client_socket.recv(1024)
                    if validate_password(receive_password, password):
                        user = user_class(client_socket)
                        user.save_user_in_cache()
                        user.check_user_in_cache()
                        print(f"User {client_socket.getpeername()[0]}:{client_socket.getpeername()[1]} connected successfully")
                    else:
                        client_socket.close()
                        print(f"Invalid password from {client_socket.getpeername()[0]}:{client_socket.getpeername()[1]}")

                else:
                    data = s.recv(1024)
                    if data:
                        print(f"Received data from {s.getpeername()[0]}:{s.getpeername()[1]}: {data.decode()}")
                    else:
                        client_sockets.remove(s)
                        s.close()
                        print(f"Client disconnected from {s.getpeername()[0]}:{s.getpeername()[1]}")


    except KeyboardInterrupt: 
        server_socket.close()
        print("Server closed")
    

def get_ip_address():
    ip = socket.gethostbyname(socket.gethostname())
    return ip
    
def get_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((get_ip_address(), 0)) != 0:
        return s.getsockname()[1]
    else:
        s.close()
        return get_free_port()


def connect_to_server(host, port, password):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(password.encode())
    return client_socket

