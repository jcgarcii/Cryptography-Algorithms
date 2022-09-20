#Part 2_1: Permutation Function


from collections import Counter
import string


def main(): 
    gather()
    userChoose()
    print("Done.")
    
def gather():   
    #collects input for the ciphertext and the ammount to shift by:  
    cipher = input('What is your cipher text?\n')   
    x = input('Which letter would you like to swap?\n')
    y = input('Which letter would you like to swap' + ' '+ x + ' ' + 'with?\n') 

    alphabet = dict.fromkeys(string.ascii_lowercase, '')
    
    #call the permutation function
    perm(cipher, alphabet, x, y) 

def gather2(permut, alphabet):   
    #collects input for the ciphertext and the ammount to shift by:  
    x = input('Which letter would you like to swap?\n')
    y = input('Which letter would you like to swap' + ' '+ x + ' ' + 'with?\n') 
    #call the permutation function
    perm(permut, alphabet, x, y) 
    
def perm(cipher, alphabet, x, y): 
    #lenAlphabet = len(alphabet)
    #shift = int(x) - int(y)
    
    
    #Permutation Changes:
    mPermut = str(cipher).lower()
    permut = mPermut.replace(x, y)
    
    #for loop to loop through entire alphabet:
    #for lenAlphabet in alphabet: 
        #found the .join(chr(ord)) online, although it seems to be built in to Python. 
    #    t = ''.join(chr((ord(lenAlphabet) - 97 - shift) %26 + 97))
    #       decrypted message
    #    finalAlphabet = finalAlphabet + t

    print("Here are your alphabet mappings: ")

    k = {x:y}
    alphabet.update(k)

    for key, value in alphabet.items(): 
        print(key, '==' + ' ' + value)
    

    #print the message for user
    print(permut) 
    userChoose(permut, alphabet)
    #print(finalAlphabet)

def userChoose(permut, alphabet):
    choice = input("Would you like to replace another character? (y/n) \n")
    print(choice)

    if str(choice) == 'y':
        gather2(permut, alphabet)
    else:
        print('Thank you, final text is: ' + permut) 
        exit() 
main()