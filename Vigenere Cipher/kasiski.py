#Lab03 Kasiski Method Helpers: 
from ast import Global
from collections import Counter
from multiprocessing.sharedctypes import Value
import string
import re
global storedCipher

def main(): 
    #initiate program:
    gather()
    #on completion:
    print('Done.')
    #Print Final Output: 
    printLine()
    print('>> Here is your final cipher: ')
    print(str(storedCipher))
    printLine()    

#input gathering method
def gather(): 
    printLine()
    cipher = input('>>' + ' ' + 'What is your ciphertext? \n')
    cipher = str(cipher).lower()
    #starts the statistics portion of the program: 
    freq(cipher)
    #starts the shifting portion of the program: 
    shifter(cipher)

#trigram frequency method
def freq(cipher):
    printLine()
    #Due to the higher number of trigrams, we ask the user to enter the number of trigrams they would like to see (e.g., '5' for the top 5 or so)
    numTrigrams = input('>>' + ' ' + 'How mnay trigrams would you like to display? \n')
    #format the string for use, initalize other variables we'll be using: 
    inumTrigrams = int(numTrigrams)
    i = 1
    lenCipher = len(cipher)
    #used to store selected number of trigrams - for use in a later function
    trigramDict = {}
    currHash = {}
    #Gather and rank the trigrams using Python collections:
    trigram = Counter(cipher[x:x+3] for x in range(lenCipher))

    #formatted output of the ranking(s):
    print('> Trigram Analysis: ') 
    for key, value in trigram.most_common():
        if(inumTrigrams == 0): 
            #break if we have iterated through the specified top trigrams, rather than continue: 
            break
        else:
            #store the selected values into a hashing structure
            currHash = {str(key):str(value)}
            trigramDict.update(currHash)
            #formatted output
            print('//' + str(i) + ':', key, value)
            #tracking variables
            inumTrigrams = inumTrigrams - 1
            i+=1
    
    keyLength(trigramDict, cipher)
    

#method counts the number of characters in-between each occurance (second letter -> first letter of the trigram)
def keyLength(trigramDict, cipher):
    printLine()
    #Initialization of tracking variables: 
    previousOccur = 0
    spaces = 0 
    iteration = 0
    #Iterate through our selected trigrams:
    for key in trigramDict:  
        #Reset tracking variables: 
        print('>> Appearances for: ',key)
        previousOccur = 0
        spaces = 0
        iteration = 0
        #Search the cipher for occurances, cycle for each occurance
        for match in re.finditer(key, cipher):
            #If first occurance (for formatting): 
            if iteration == 0:
                spaces = (int(match.start()) + 1) - previousOccur
                print('// First Occurance: ', spaces)
                iteration += 1
            #Counts the spaces in between, starting at the second character in the trigram until the first occurence: 
            else: 
                spaces = (int(match.start()) + 1) - previousOccur
                previousOccur = match.start() + 1 
                print('// Spaces till Next Occurance' , spaces)
        
        print('')

#character performs singular character analysis to use alongside the trigram frequency analysis: 
def freqCount(cipher, x, display, keyLen):
    printLine() 
    s = len(cipher)
    j = 1
    k = 1
    iDisplay = display
    currCipher = ''

    #for every ith character in a sequence, collect the character:
    for s in cipher: 
        if j%keyLen == x: 
            currCipher = currCipher + s
        j+=1

    #print out the frequency, with sepcified # of characters 
    print('>> Here is your mono-aphabetic frequency analysis for the '+ str(x + 1) + 'th character')
    freqCount = Counter(currCipher)
    q = len(cipher)
    q = int(q)
    for keys, value in freqCount.most_common():
        if iDisplay <= 0:
            break
        else: 
            p = str(round((value / q) * 100, 1))
            print('#' + str(k) + ':', keys, p + '%')
            k+=1
            iDisplay = iDisplay -1
    
        
            
#    print('>> Here is your mono-aphabetic frequency analysis for the '+ str(x + 1) + 'th character')
#    for key, value in freq.most_common(): 
#        if display <= 0 :
#            break
#        else:
            #first iteration case:
#            if j == 0: 
#                if i == 0:
#                    k = str(round((value / s) *100, 1))
#                    print('// ', key, k, '%') 
#                    display = display - 1
            #rest of the cases:
#            else: 
#                if j%i == 0:         
#                    k = str(round((value / s) *100, 1))
#                    print('// ', key, k, '%')
#                    display = display - 1
#           j = j + keyLen


#initiates a series of user inputs, and prints out the character analysis for every ith character in the key:        
def shifter(cipher):
    printLine()
    #Indictate the keylength:
    keyLen = input('>> What is your Key Length? \n')
    keyLen = int(keyLen)
    display = input('>> How many characters in the singular frequency analysis would you like to display? \n')
    display = int(display)
    #X - monoalphabetic frequency analysis: 
    for x in range(keyLen): 
        freqCount(cipher, x, display, keyLen)
    
    howMany(keyLen, cipher)
    
#Allows user to choose which character they would like to shift, and by how much:
def howMany(i, cipher):
    #input variables: 
    invalidInput = ''
    finishedCheck = ''
    #track the current cipher iteration after shift(s)
    currCipher = ''
    #Alphabet for reference: 
    alphabetPrint()
    #Collect which character in sequence a user would like to shift:
    key = input('>> What do you suspect your key to be? (must be same length as key provided) \n')
    lKey = len(key)
    
    #check to see if input is valid
    if lKey == i: 
        #Shift the indicated character(s)
        shiftByN(key, cipher)
        
        #Check to see if user would like to shift another char: 
        finishedCheck = input('>> Would you like to try another key? (Y/N) \n')
        finishedCheck = str(finishedCheck).lower()     
        if(finishedCheck == 'y'): 
            howMany(i, cipher)
        else: 
            print('')
            
    #if invalid, ask if they would like to try again 
    else: 
        invalidInput = input('>> Invalid Input, try again? (Y/N) \n') 
        invalidInput = str(invalidInput).lower()

        if(invalidInput == 'y'): 
            howMany(i, cipher)
        else: 
            print('')

#shifts a ith character in the potential key              
def shiftByN(key, cipher): 
    
    s = len(cipher)
    k = len(key)

    decrypted = ''
    l = ''

    x = 0
    j = ord(key[x]) - 97

    #shift by n
    for s in cipher: 
        l = ''.join(chr((ord(s) - 97 - j) %26 + 97))
        #decrypted message
        decrypted = decrypted + l
        x = x + 1
        if x >= 0 and x < k:
            j = ord(key[x]) - 97    
        else: 
            x = 0
            j = ord(key[x]) - 97
            
    storeCipher(decrypted)
    printItr(decrypted)

    
#prints the alphabet to provide context for our user:
def alphabetPrint():
    printLine()
    alphabet = dict.fromkeys(string.ascii_lowercase, '')
    n = 1
    for keys, values in alphabet.items():
        print(str(keys) + ' shifts by:' + str(n))
        n = n+1
    
#Stores the most recent cipher:
def storeCipher(decrypted):
    global storedCipher
    storedCipher = decrypted
    print('')

#Prints Current Iteration:   
def printItr(decrypted): 
    print('--------------------------------')
    print('>> Current Iteration: ')
    print(decrypted)
    print('--------------------------------')

#Maintains a structure to our output
def printLine(): 
    print('======================================================================================================')

main() 