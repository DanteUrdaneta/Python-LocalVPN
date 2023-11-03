from modules.functions import *
from modules.security_functions import check_password


def menu():
    print("1. Create server")
    print("2. Connect to server")
    print("3. Exit")
    return int(input("Enter your choice: "))


def create():
    print("Please enter the password:")
    password = input()
    port = get_free_port()
    ip = get_ip_address()
    if check_password(password):
        print(f"Created server on port {port} with IP address {ip}")
        create_server(ip,port, password)
        print("Server created successfully")
    else:
        print("Invalid password. Please try again.")


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