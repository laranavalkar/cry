import pyAesCrypt
bufferSize = 128 * 1024
password = "Lara"

pyAesCrypt.encryptFile(r"C:\Users\Romil\AppData\Local\Programs\Python\Python39\CRYPTO practs\data.txt", "data.txt.aes",password,bufferSize)

pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt",password,bufferSize)
