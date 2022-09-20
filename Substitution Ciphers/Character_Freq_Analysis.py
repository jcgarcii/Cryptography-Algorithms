from collections import Counter
#Part 2
def main():
    gather()
    print("Done.")

def gather():   
    #collects input for the ciphertext:  
    cipher = input('What is your cipher text?\n')   
    
    frequency(cipher)
    di_freq(cipher)
    tri_freq(cipher)

def frequency(cipher):
    cipher = cipher.lower()
    s = len(cipher)
    #side note: very cool how Python has a hashing table built-in!
    freq = Counter(cipher)

    print('==================================')
    print("Here are your mono-values: \n")
    print('==================================')

    printOrdered(freq)
    printFreq(freq, s)

def di_freq(cipher):
    cipher = cipher.lower()
    k = len(cipher)

    print('==================================')
    print("Here are your digram values: \n")
    print('==================================')

    di = Counter(cipher[x:x+2] for x in range(k))

    printOrdered(di) 

def tri_freq(cipher):
    cipher = cipher.lower()
    j = len(cipher)
    print('==================================')
    print("Here are your trigram values: \n")
    print('==================================')

    tri = Counter(cipher[x:x+3] for x in range(j))
    
    printOrdered(tri)
#############################PRINTERS############################################

#Prints the recurrance of each character in decending order
def printOrdered(freq): 
    print('1.) In Order: ')
    print(' ' + str(freq)) 
    print('--------------------------------')

#Prints the key, and the value associated with that key in frequency format as they appear
def printFreq(freq, s): 
    
    print('2.) In Frequency Format: (unordered)')
    
    for key, value in freq.items(): 
        k = str(round((value / s) *100, 1))
        print(key, k +'%')

    print('--------------------------------') 

main()   