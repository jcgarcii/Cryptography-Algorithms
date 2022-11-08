import string
#Part 3
def main():
    gather()
    print("Done.")

def gather():
    choice = input("Would you like to (1) decrypt or (2) encrypt? [Enter 1 or 2] \n")
    cipher = input("What is your text?")

    if str(choice) == '1':
        decrypt(cipher)
    if str(choice) == '2':
        encrypt(cipher) 
    

def encrypt(cipher): 
    cipher = cipher.translate(str.maketrans('','', string.punctuation))
    mCipher = ''.join(cipher.split())
    mCipher = mCipher.lower()

    key = 'rubi'
    s = len(mCipher)
    k = len(key)

    l = ''
    encrypted = ''
    n = 0
    
    for k in key: 
        n = ord(k) 
        #for loop to loop through entire text:
        for s in mCipher:  
            l = ''.join(chr((ord(s) - 97 - n) %26 + 97))
            #decrypted message
            encrypted = encrypted + l
    print(encrypted[:len(mCipher)])


def decrypt(cipher): 
    cipher = cipher.translate(str.maketrans('','', string.punctuation))
    mCipher = ''.join(cipher.split())

    key = 'rubi'
    s = len(mCipher)
    k = len(key)

    l = ''
    decrypted = ''
    n = 0

    for k in key: 
        n = ord(k)
        #for loop to loop through entire text:
        for s in mCipher:  
            l = ''.join(chr((ord(s) - 97 + n) %26 + 97))
            #decrypted message
            decrypted = decrypted + l

    print(decrypted[:len(mCipher)])

main()