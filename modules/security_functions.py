
#middleware fuction that validate password to connect
def validate_password(receive_password, password):
    if receive_password == password:
        return True
    else:
        return False


#middleware fuction that validate password to create server
def check_password(password):
    if len(password) < 8:
        print("Password must have at least 8 characters")
        return False 
    else:
        return True