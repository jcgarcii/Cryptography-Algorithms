#Returns the most common element in a list
from collections import Counter
from functools import reduce


def mostCommon(lst):
    element = Counter(lst)
    return max(lst, key = element.get)

#Used to calculate m[0]
def flaw1(file):
    x = ''
    c = ''
    calculation = 0
    with open(file, "r") as f:
        arr = []
        for line in f:
            entry = line.strip().split(' ')       # Entry      = ['0X01FF00', '0XDB']
            #Entries;
            x = entry[0]
            c = entry[1]
            #Convert:
            x = int(x[-2:],16)  
            c = int(c[-2:],16)
            #Calculation:
            calculation = c ^ ((x + 2) % 256)
            arr.append(calculation) # IMPLEMENT HERE
        
        return mostCommon(arr)        
#Used to calculate k[0]
def flaw2(file, m):
    c = ''
    x = ''

    with open(file, "r") as f:
        arr = []
        for line in f:
            entry = line.strip().split(' ')       # Entry      = ['0X01FF00', '0XDB']
            #Entries;
            x = entry[0]
            c = entry[1]
            #Convert:
            x = int(x[-2:],16)  
            c = int(c[-2:],16)
            #Calculate: 
            calculation = (c ^ m) - x - 6 
            arr.append(calculation) # IMPLEMENT HERE
        return mostCommon(arr)
 
#Used to calculate k
def flaw2b(file, k, m):
    c = ''
    x = ''

    with open(file, "r") as f:
        arr = []
        for line in f:
            entry = line.strip().split(' ')       # Entry      = ['0X01FF00', '0XDB']
            #Entries;
            x = entry[0]
            c = entry[1]
            #Convert:
            x = int(x[-2:],16)  
            c = int(c[-2:],16)
            #Calculate: 
            calculation = ((c ^ m) - x - 10 - k) % 256
            arr.append(calculation) # IMPLEMENT HERE
        return mostCommon(arr)  

#Used to calculate k[1], k[2], ... k[12]
def flaw3(file, m, k, n, soFar):
    c = ''
    x = ''
    with open(file, "r") as f:
        arr = []
        for line in f:
            entry = line.strip().split(' ')       # Entry      = ['0X01FF00', '0XDB']
             #Entries;
            x = entry[0]
            c = entry[1]
            #Convert:
            x = int(x[-2:],16)  
            c = int(c[-2:],16)
            #Calculate: 
            calculation = ((c ^ m) - x - n - soFar) % 256
            arr.append(calculation)  # IMPLEMENT HERE
        return mostCommon(arr)
    
def main():
    #Files used: 
    file1 = 'bytes_01FFXX.txt'
    file2 = 'bytes_03FFXX.txt'
    file2a = 'bytes_04FFXX.txt'
    file3a = 'bytes_0'
    file3b = 'FFXX.txt'
    #for use in Flaw 3: 
    key = []
    num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    #Flaw 1: 
    m = flaw1(file1)

    #Flaw 2: 
    k = flaw2(file2, m)
    k2 = flaw2b(file2a, k, m) 
    
    #Flaw3:
    #add k to our key
    key.append(k)
    key.append(k2)
    #initialize the vars to be used: 
    soFar = _sum(key)
    n = _sum(num[0:5])
    #idx to be used for math portion:
    currIdx = 6
    hexDec = 5
    file3 = file3a + str(hex(hexDec)[-1:]) + file3b

    for i in range(11): 
        #pass in our vars: 
        ret = flaw3(file3, m, k, n, soFar)
        key.append(ret)
        #print('Previous Stuff',i ,': ', str(n), str(soFar))
        #update sums:
        n = _sum(num[0:currIdx])
        soFar = _sum(key)
        #update tracking vars:
        hexDec = hexDec + 1
        currIdx = currIdx + 1
        #update file:
        file3 = file3a + str(hex(hexDec)[-1:]) + file3b

    printKey(m, key)
    
#helper sum function: 
def _sum(arr):
    sum = reduce(lambda a, b: a+b, arr)
    return(sum)

#Prints the Guess: 
def printKey(m, key): 
    i = 0
    l = '' 
    print('Guess for m[0]: ', m)
    for x in key:
        print('Guess for k[',str(i),']: ' , hex(x))
        i += 1
        l = l + str(hex(x)).replace('0x','')
    
    message = decoder(l)
    print('Here is your message: ', message)

#Converts from hex to key: 
def decoder(key):
    bytes_object = bytes.fromhex(key)
    ascii_string = bytes_object.decode('ASCII')
    
    return ascii_string

if __name__ == '__main__':
    main()
