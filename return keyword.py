s_username = "EMC"
s_password = "123"

uname = input("Enter username :" )
password = input("Enter password :" )

def validate():
    if (s_username==uname and s_password==password):
        return True
    else:
        return False
validate()
