import re

password=input('Enter your password:')
if len(password)<8:
#Password must be of atleast 8 characters.    
    print('Password must be of atleast 8 characters.')
#Password must contain atleast one uppercase letter.    
elif not re.search(['A-Z'],password):
    print('Password must contain atleast one uppercase letter.')
#Password must contain atleast one lowercase character.
elif not re.search(['a-z'],password):
    print("Password must contain atleast one lowercase letter.")
#Password must contain atleast one number.
elif not re.search(['0-9'],password):
    print("Password must contain atleast one number.")
else: 
    print("Password is strong.")    
