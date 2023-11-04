from modules.functions import get_free_port, get_ip_address, connect_to_server
from modules.functions import server_class
from modules.security_functions import check_password
from modules.user import user_class


def menu():
    print("1. Create server")
    print("2. Connect to server")
    print("3. configure user")
    print("4. Exit")
    return int(input("Enter your choice: "))


def create():
    print("Please enter the password:")
    password = input()
    port = get_free_port()
    ip = get_ip_address()
    if check_password(password):
        print(f"Created server on port {port} with IP address {ip}")
        server = server_class(ip, port, password)
        server.create_server()
        print("Server created successfully")
    else:
        print("Invalid password. Please try again.")


def configure_user():
    print("Please enter the username:")
    username = input()
    user = user_class(username)
    if user.check_user_in_cache():
        print("User already exists")
    else:
        user.save_user_in_cache()
        print("User created successfully")

def connect():
    try:
        print("Please enter the ip address: ")
        ip = input()
        print("Please enter the port: ")
        port = int(input())
        print("Please enter the password: ")
        password = input()
        connect_to_server(ip, port, password)
    except:
        print("Invalid input. Please try again.")




def app():
    while True:
        choice = menu()
        if choice == 1:
            create()
       
        elif choice == 2:
            connect()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")