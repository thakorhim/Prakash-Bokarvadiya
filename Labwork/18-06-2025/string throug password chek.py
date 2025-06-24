#string through password check
#one by one character  chek

def password_check(password):
    special_char = ['$','@','#']
    val = True

    if len(password)<6:
        print('length should be at least 6')
        val = False

    if len(password)>16:
        print('length should be not be greater than 16')
        val = False

    if not any(char.isdigit() for char in password):
        print('password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in password):
        print('password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in password):
        print('password should have at least one lowercase letter')
        val = False

    if not any(char in special_char for char in password):
        print('password should have at least one of the symbols $@#')
        val = False

    if val:
        return val

password = input('enter password:')
if(password_check(password)):
    print('password is valid')
else:
    print('invalid password') 