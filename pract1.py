#PRACT1
import bcrypt

password = b'Password'

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

print("Salt :")
print(salt)


print("Hashed :")
print(hashed)


