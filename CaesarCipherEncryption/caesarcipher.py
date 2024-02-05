string = "HI i am Ashesh Jyoti"
def encrypt(key_,message_):
    msg= message_
    key =int(key_)
    msg = msg.rsplit()
    encrypt=""
    for i in msg:
        for j in i:
            encrypt = encrypt+(chr(ord(j)+key))
        encrypt = encrypt+" "
    return encrypt
def decrypt(key_,message_):
    key = int(key_)
    msg = message_
    msg = msg.rsplit()
    decrypted = ""
    for i in msg:
        for j in i:
            decrypted = decrypted+chr(ord(j)-3)
        decrypted = decrypted+" "
    return decrypted
encrptd = encrypt(3,'HI i am Ashesh Jyoti')
decrptd = decrypt(3,encrptd)
print("encrypted:",encrptd)
print("decrypted:",decrptd)