import subprocess

def des_encrypt(text, key):
    #Use openssl to encrypt the data
    command = "/bin/echo -n " + text + " | openssl enc -a -des-cbc -nosalt -iv 0000000000000000 -K " + key + " -A  | xxd"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = proc.stdout.readlines()

    base64String = ""
    for i in range(len(output)):
        #We must parse the ciphertext out of the outout
        #output[i] = [b'00000000: 3172 3973 5850 6644 5431 4737 7737 4149  1r9sXPfDT1G7w7AI\n']
        line = str(output[i]).split(" ")
        string = str(line[len(line)-1])
        base64String = base64String + string[:-3]
    return base64String
  
def des_decrypt(ciphertext, key):
    #Use openssl to decrypt the data
    command = "/bin/echo -n " + ciphertext + " | openssl enc -d -a -des-cbc -nosalt -iv 0000000000000000 -A -K " + key + " | xxd"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = proc.stdout.readlines()
    
    base64String = ""
    for i in range(len(output)):
        #We must parse the ciphertext out of the outout
        #output[i] = [b'00000000: 3172 3973 5850 6644 5431 4737 7737 4149  1r9sXPfDT1G7w7AI\n']
        line = str(output[i]).split(" ")
        string = str(line[len(line)-1])
        base64String = base64String + string[:-3]
    return base64String

def nextHex(num): 
    num = int(num, 16) + 1 
    next = hex(num)     
    next = str(next).replace('0x' , '')
    
    i = len(next)

    if(i == 1): 
        next = '0' + next 
    print('Hex: ' , next)
    
    return next 

def main():
    #TODO: Implement code here
    #You may write additional functions as needed
    plaintext = 'Tatooine'
    ciphertext = 'tm97RIBRG3eY8fkb0iU696gHGhfGxnYZGVcB2sJRDK4='
    secretMSG = 'eM+KmLs+5TFQEknuRX2fzhigcZPCkSho7bf/73mh8bFaHaCFLW7AoQ=='
    encrypted = ''
    decrypted = ''
    key1 = '319df2f409baee'
    key2 = '64abc398ac4fee'
    flag = False
    i = '00'
    j = '00'

    for x in range (0, 255): 
        k1 = key1 + i
        encrypted = des_encrypt(plaintext, k1)
        
        for y in range (0,255):
            k2 = key2 + j
            print('Trying k1='+ str(k1), '\nand k2=' + str(k2)) 

            decrypted = des_decrypt(ciphertext, k2)

            if(decrypted == encrypted): 
                print('------MATCH FOUND---------')
                flag = True
                break 
            
            j = nextHex(j)
            
        if(flag == True):
            print('Found K1=' + k1)
            print('Found K2=' + k2)
            secret = des_decrypt(secretMSG, k2)
            secret = des_decrypt(secret, k1)
            print(secret)
            break
        
        j = '00'
        
        i = nextHex(i)

if __name__ == '__main__':
    main()

