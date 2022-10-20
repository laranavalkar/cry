#PRACT2
import hashlib

password = 'Password'

salt="Sgz"

dataBase_password=password+salt

hashed=hashlib.md5(dataBase_password.encode())

print(hashed.hexdigest())
