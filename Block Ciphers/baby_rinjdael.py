#Implements Baby Rinjdael:
def printRound(x): 
    print('================ Round:' + x + '=========================')

#subbytes function: 
def subBytes(hexDec):
    swapW = ''
    table = {'0':'a', 
             '1':'4', 
             '2':'3',
             '3':'b',
             '4':'8',
             '5':'e', 
             '6':'2',
             '7':'c',
             '8':'5',
             '9':'7',
             'a':'6',
             'b':'f', 
             'c':'0',
             'd':'1',
             'e':'9',
             'f':'d'}
    swapW = table.get(hexDec)
    return swapW

#swap the second row's funcitons: 
def shiftRow(hexInput):
    newHex = str(hexInput[0]) + str(hexInput[3]) + str(hexInput[2]) + str(hexInput[1])   
    
    return newHex

#Coloumn Mix Function: 
def mixColoumn(hexInput):
    k0 = str(bin(int(hexInput[0], 16))).replace('0b', '').zfill(4)
    k1 = str(bin(int(hexInput[1], 16))).replace('0b', '').zfill(4)
    k2 = str(bin(int(hexInput[2], 16))).replace('0b', '').zfill(4)
    k3 = str(bin(int(hexInput[3], 16))).replace('0b', '').zfill(4)

    #Hexadigit 1: 
    h00 = int(k0[0])
    h01 = int(k0[1])
    h02 = int(k0[2])
    h03 = int(k0[3])
    #Hexadigit 2: 
    h10 = int(k1[0])
    h11 = int(k1[1])
    h12 = int(k1[2])
    h13 = int(k1[3])
    #Hexadigit 3: 
    h20 = int(k2[0])
    h21 = int(k2[1])
    h22 = int(k2[2])
    h23 = int(k2[3])
    #Hexadigit 4: 
    h30 = int(k3[0])
    h31 = int(k3[1])
    h32 = int(k3[2])
    h33 = int(k3[3])
    #new values: 
    #Hexadigit 1: 
    mH00 = str((h00 + h02 + h12 + h13) % 2)
    mH01 = str((h00 + h01 + h03 + h13) % 2)
    mH02 = str((h00 + h01 + h02 + h10) % 2) 
    mH03 = str((h01 + h03 + h11 + h12 + h13) % 2) 
    mK0 = mH00 + mH01 + mH02 + mH03 
    #Hexadigit 2: 
    mH10 =  str((h02 + h03 + h10 + h12) % 2)
    mH11 =  str((h03 + h10 + h11 + h13) % 2)
    mH12 =  str((h00 + h10 + h11 + h12) % 2)
    mH13 =  str((h01 + h02 + h03 + h11+ h13) % 2)
    mK1 = mH10 + mH11 + mH12 + mH13
    #Hexadigit 3: 
    mH20 =  str((h20 + h22 + h32 + h33) % 2)
    mH21 =  str((h20 + h21 + h23 + h33) % 2)
    mH22 =  str((h20 + h21 + h22 + h30) % 2)
    mH23 =  str((h21 + h23 + h31 + h32 + h33) % 2)
    mK2 = mH20 + mH21 + mH22 + mH23 
    #Hexadigit 4: 
    mH30 =  str((h22 + h23 + h30 + h32) % 2)
    mH31 =  str((h23 + h30 + h31 + h33) % 2)
    mH32 =  str((h20 + h30 + h31 + h32) % 2)
    mH33 =  str((h21 + h22 + h23 + h31 + h33) % 2) 
    mK3 = mH30 + mH31 + mH32 + mH33

    hexOut = str(hex(int(mK0 + mK1 + mK2 + mK3, 2))).replace('0x', '')
    return hexOut

#toMatrix function:
def toMatrix(hexInput): 
    ans = []
    inBinary = ''
    k = 0 
    #retrieve the correct format: 
    for i in range(0, 4):
        temp = str(bin(int(hexInput[i], 16))).replace('0b', '')
        k = len(temp) 
        if(k < 4):
            #formatting: 
            if(k == 3): 
                temp = '0' + temp 
            elif(k ==2): 
                temp = '00' + temp 
            elif(k == 1): 
                temp = '000' + temp
        inBinary = inBinary + temp
        
    binMatrix = [[inBinary[0],inBinary[8]],
                 [inBinary[1],inBinary[9]],
                 [inBinary[2],inBinary[10]],
                 [inBinary[3],inBinary[11]],
                 [inBinary[4],inBinary[12]],
                 [inBinary[5],inBinary[13]],
                 [inBinary[6],inBinary[14]],
                 [inBinary[7],inBinary[15]]]

    hexMatrix = [[hexInput[0], hexInput[2]], 
                 [hexInput[1], hexInput[3]]]

    print('Binary Matrix:'
            + '\n' + str(binMatrix[0]) 
            + '\n' + str(binMatrix[1])
            + '\n' + str(binMatrix[2])
            + '\n' + str(binMatrix[3])
            + '\n' + str(binMatrix[4])
            + '\n' + str(binMatrix[5])
            + '\n' + str(binMatrix[6])
            + '\n' + str(binMatrix[7]))                 

    print('Hexadecimal Matrix: \n'
                + str(hexMatrix[0])
                + '\n' + str(hexMatrix[1]))
    
    #Returns the Matrix's in format [Binary Matrix, Hexadecimal Matrix]:
    ans.append(binMatrix)
    ans.append(hexMatrix)
    return ans

def main():
    x = 'Input'
    key = int('6b5d', 16)
    #Collect the Hexadecimals to Encrypt:
    hexInput = input('Enter your 4 hexadecimals\n>> ')
    hexInput = int(hexInput, 16)
    
    mHex0 = key ^ hexInput
    mHex0 = str(hex(mHex0)).replace('0x', '')

    printRound(x)
    returned = toMatrix(mHex0)
    #---------------Round 1:-------------------------------#
    x = '1'
    key = int('6538', 16)
    printRound(x)

    #1.) SubBytes: 
    mHex1 = ''
    for i in mHex0: 
        mHex1 = mHex1 + subBytes(i)
    #2.) Shift Row: 
    mHex1 = shiftRow(mHex1)
    #3.) Mix Coloumn: 
    mHex1 = mixColoumn(mHex1)
    #4.) XOR, retrieve next cycle: 
    mHex1 = key ^ int(mHex1, 16)
    mHex1 = str(hex(mHex1)).replace('0x', '')
    returned = toMatrix(mHex1)
    #----------------Round 2:------------------------------#
    x = '2'
    key = int('1e26', 16)
    printRound(x)

    #1.) SubBytes: 
    mHex2 = ''
    for i in mHex1: 
        mHex2 = mHex2 + subBytes(i)
    #2.) Shift Row: 
    mHex2 = shiftRow(mHex2)
    #3.) Mix Coloumn: 
    mHex2 = mixColoumn(mHex2)
    #4.) XOR, retrieve next cycle: 
    mHex2 = key ^ int(mHex2, 16)
    mHex2 = str(hex(mHex2)).replace('0x', '')
    returned = toMatrix(mHex2)

    #---------------Round 3:-------------------------------#
    x = '3'
    key = int('7d5b', 16)
    printRound(x)

    #1.) SubBytes: 
    mHex3 = ''
    for i in mHex2: 
        mHex3 = mHex3 + subBytes(i)
    #2.) Shift Row: 
    mHex3 = shiftRow(mHex3)
    #3.) Mix Coloumn: 
    mHex3 = mixColoumn(mHex3)
    #4.) XOR, retrieve next cycle: 
    mHex3 = key ^ int(mHex3, 16)
    mHex3 = str(hex(mHex3)).replace('0x', '')
    returned = toMatrix(mHex3)

    #---------------Round 4: ------------------------------#
    x = '4'
    key = int('0358', 16)
    printRound(x)
    
    #1.) SubBytes: 
    mHex4 = ''
    for i in mHex3: 
        mHex4 = mHex4 + subBytes(i)
    #2.) Shift Row: 
    mHex4 = shiftRow(mHex4)
    #4.) XOR, retrieve next cycle: 
    mHex4 = key ^ int(mHex4, 16)
    mHex4 = str(hex(mHex4)).replace('0x', '')
    returned = toMatrix(mHex4)    
    #---------------Output:--------------------------------#
    x = 'Output'
    printRound(x)
    returned = toMatrix(mHex4)  

main() 