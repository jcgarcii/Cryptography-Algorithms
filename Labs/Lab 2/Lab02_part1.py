#Part 1: 

def main(): 
    gather()
    print("Done.")
    
def gather():   
    #collects input for the ciphertext and the ammount to shift by:  
    cipher = input('What is your cipher text?\n')   
    x = input('How much would you like to shift by?\n')

    #call the shift function:
    shift(cipher, x) 
    
def shift(cipher, x):
    #seting up variables to be used
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    n = int(x)
    s = len(cipher)
    k = len(alphabet)

    decrypted = ''
    finalAlphabet = ''

    #for loop to loop through entire text:
    for s in cipher: 
        #found the .join(chr(ord)) online, although it seems to be built in to Python. 
        l = ''.join(chr((ord(s) - 97 - n) %26 + 97))
        #decrypted message
        decrypted = decrypted + l
    
    #for loop to loop through entire alphabet:
    for k in alphabet: 
        #found the .join(chr(ord)) online, although it seems to be built in to Python. 
        t = ''.join(chr((ord(k) - 97 - n) %26 + 97))
        #decrypted message
        finalAlphabet = finalAlphabet + t

    #print the message for user
    print(decrypted) 
    print(finalAlphabet)

main()