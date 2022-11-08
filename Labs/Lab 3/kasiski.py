#Lab03 Kasiski Method: 
from collections import Counter
import string
import re

def main(): 
    gather()
    print('Done.')

#input gathering method
def gather(): 
    print('======================================================================================================')
    cipher = input('>>' + ' ' + 'What is your ciphertext?')
    cipher = str(cipher)
    freq(cipher)

#trigram frequency method
def freq(cipher):
    print('======================================================================================================')
    #Due to the higher number of trigrams, we ask the user to enter the number of trigrams they would like to see (e.g., '5' for the top 5 or so)
    numTrigrams = input('>>' + ' ' + 'How mnay trigrams would you like to display?')
    #format the string for use, initalize other variables we'll be using: 
    inumTrigrams = int(numTrigrams)
    i = 1
    cipher = cipher.lower()
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
    
    keyLength(trigramDict, cipher, lenCipher, numTrigrams)

#method counts the number of characters in-between each occurance (second letter -> first letter of the trigram)
def keyLength(trigramDict, cipher, lenCipher, numTrigams):
    print('======================================================================================================')
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

    print('test')

main() 