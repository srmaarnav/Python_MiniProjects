print('Create your account')

username = input('Enter Username : ')
password = input('Enter Password : ')

print('Your account has been created successfully!')
print('\nLogin Now')

uname = input('Username : ')
passw = input('Password : ')

if ((username == uname) and (passw == password)):
    print('Login Successful')
else:
    print('Login Failed.')