#This Implement a Baby Feistel - taking in the first four bits of a character



#substitution box function:
def _sbox(key, R): 
    i = 10

    a = '10' 
    b = '01'
    c = '00'
    d = '11'

    R = str(R)
    if(len(R) == 1): 
        R = '0' + R

    if R == a : 
        i = 0 
    
    elif R == b: 
        i = 1 
    
    elif R == c: 
        i = 2
    
    elif R == d : 
        i = 3
    
    else:
        print('lol bruh')

    table = {'0000':['10', '10', '00', '11'],
             '0001':['00', '11', '10', '00'],
             '0010':['00', '10', '01',  '00'],
             '0011':['01', '00', '11', '11'],
             '0100':['11', '00', '10',  '01'],
             '0101':['10', '11', '01', '10'],
             '0110':['11', '01', '11', '10'],
             '0111':['10', '01', '00',  '01'],
             '1000':['00', '01', '11', '10'],
             '1001':['01', '00', '01',  '11'],
             '1010':['11', '11', '00', '00'],
             '1011':['11', '10', '01',  '01'],
             '1100':['01', '11', '10', '10'],
             '1101':['00', '01', '11',  '00'],
             '1110':['10', '00', '00', '01'],
             '1111':['01', '10', '10',  '11']}

    selection = table.get(key)
    selection = selection[i]
    return selection

def round(L, R, Key):
    #variables to be used: 
    mR = 0
    round = []
    newKey = ''

    #Get S-Box values:
    box = _sbox(Key, R)  
    #Caculated the new Right:
    mR = int(L,2) ^ int(box, 2) 

    mR = bin(mR)
    mR = str(mR).replace('0b', '')[-2:]
    
    #Shift key: 
    newKey = Key[1] + Key[2] + Key[3] + Key[0]
    
    #Return answers in format: round[new Right, Left, new Key]
    round.append(mR)
    round.append(R)
    round.append(newKey)

    return round 

def deRound(L, R, Key): 
    #variables to be used: 
    mL = 0
    round = []
    newKey = ''
    
    #Get S-Box values:
    box = _sbox(Key, R)  
    #Caculated the new Right:
    mL = int(L,2) ^ int(box, 2) 
    mL = bin(mL)
    mL = str(mL).replace('0b', '')[-2:]
    
    #Shift key: 
    newKey = Key[3] + Key[0] + Key[1] + Key[2]
    
    #Return answers in format: round[old Left, old Right, new Key]
    round.append(mL)
    round.append(R)
    round.append(newKey)

    return round 

def printCipher(L, R):
    str(L)
    str(R) 

    if(len(L) == 1): 
        L = '0' + L
    if(len(R) == 1): 
        R = '0' + R
    
    cipherT = L + R 
    return cipherT

def printLine():
    print('============================================================')

#takes the first four bits of a char, returns the encrypted character:
def encrypt(plaintext):
    #cycle 1, inititialization: 
    next = []
    encryption = []
    i = 1
    lPlaintext = plaintext[0:2]
    rPlaintext = plaintext[-2:]

    print('Left: ' , lPlaintext)
    print('Right: ', rPlaintext)

    key = input('Enter your starting key: \n>>')
    printLine()
    print('Encryption Process: ')
    print('Round', i, ':')

    #begin: 
    next = round(lPlaintext, rPlaintext, key)
    cipher = printCipher(next[1], next[0])
    print(cipher)
    i+=1

    #cycle 2: 
    print('Round', i, ':')
    next = round(next[1], next[0], next[2])
    cipher = printCipher(next[1], next[0])
    print(cipher)
    i+=1
    lastKey = next[2]

    #cycle 3:
    print('Round', i, ':')
    next = round(next[1], next[0], next[2])
    cipher = printCipher(next[1], next[0])
    print(cipher)
    i+=1

    encryption.append(cipher)
    encryption.append(lastKey)

    printLine() 

    return encryption
    
def decrypt(cipher, lastKey):
    #cycle 1, inititialization: 
    next = []
    i = 3
    lPlaintext = cipher[0:2]
    rPlaintext = cipher[-2:]
    print('To Decrypt: ', cipher)
    print('Last Key: ', lastKey)

    printLine()
    print('Decyrption Process: ')

    print('Round', i, ':')

    #begin: 
    next = deRound(rPlaintext, lPlaintext, lastKey)
    cipher = printCipher(next[0], next[1])
    print(cipher)
    i-=1

    #cycle 2: 
    print('Round', i, ':')
    next = deRound(next[1], next[0], next[2])
    cipher = printCipher(next[0], next[1])
    print(cipher)
    i-=1

    #cycle 3:
    print('Round', i, ':')
    next = deRound(next[1], next[0], next[2])    
    cipher = printCipher(next[0], next[1])
    print(cipher)
    i-=1

    printLine
    
#Main Function:
def main(): 
    #vars:
    encryption = []

    #Collect Input: 
    mChar = input('Hello, please enter a "character": \n>>')
    print('You have entered:', mChar)

    #Encrypt:
    encryption = encrypt(str(mChar))

    #Decrypt: 
    decrypt(encryption[0], encryption[1])

main() 
