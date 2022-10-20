from stegano import lsb
secret = lsb.hide(r"C:\Users\Romil\AppData\Local\Programs\Python\Python39\CRYPTO practs\doggie.jpg","Lara")
secret.save(r"C:\Users\Romil\AppData\Local\Programs\Python\Python39\CRYPTO practs\steg_op.png")
clear_message = lsb.reveal(r"C:\Users\Romil\AppData\Local\Programs\Python\Python39\CRYPTO practs\steg_op.png")
print(clear_message)
