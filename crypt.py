if __name__=="__main__":
    exit()

from cryptography.fernet import Fernet

def Xor(key,password):
    try:
        f = Fernet(key)
        return f.encrypt(password)
    except:
        return "Failed"

def deXor(key,crypted):
    try:
        f = Fernet(key)
        return f.decrypt(crypted)
    except:
        return "Failed"
