import sys
from getpass import getpass
import pyAesCrypt
while True:
    try:
        if len(sys.argv)!=3 or (sys.argv[1] != "e" and sys.argv[1] != "d"):
            print("Usage:")
            print("python cryptomatic.py <e>/<d> <filename with extension>")
            print("e: encryption")
            print("d: decryption")
            break
        a = sys.argv[1]
        b = sys.argv[2]
        c = sys.argv[2].split(".")[1]
        def sfrl(dir):
            password = getpass("[!] Password for encryption: ")
            bufferSize = 512*1024
            pyAesCrypt.encryptFile(str(dir),str(dir)+".aes", password, bufferSize)
            print("[*] The file is encrypted,", str(dir)+".aes")
        def sfrcz(dir):
            password = getpass("[!] Password for decryption: ")
            bufferSize = 512*1024
            pyAesCrypt.decryptFile(str(dir),str(dir)+"."+c, password, bufferSize)
            print("[*] The file is decrypted,", str(dir)+"."+c)
        if a == "e":
            sfrl(b)
            break
        elif a == "d":
            sfrcz(b)
            break
    except:
        print("[!] The password is incorrect or an unexpected error has occurred...")