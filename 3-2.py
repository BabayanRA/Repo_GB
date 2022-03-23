def user(f_name, name, birthday, email, city, p_number):
    return print(name, f_name, birthday, city, email, p_number)


user(name=input("Name:"), f_name=input("First Name:"), birthday=input("Birthdate:"), city=input("City:"),
     email=input("E-mail:"), p_number=input("Phone number:"))
