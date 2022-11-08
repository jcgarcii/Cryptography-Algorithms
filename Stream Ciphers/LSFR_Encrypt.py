# Lab 05 Part 01 Skeleton code for LFSR cryptosystem
import binascii
import sys


#The cycle function produces the new bit, shifts the registers to the right by one position,
#and puts the new bit in the 4th bit position.
#As it is written it XORs the first bit and the last bit in the registers
#You may need to select different bits to create the correct xorValue
#However, the shifting of the registers will not need to be modified.
def cycle(registers):
  xorValue = ((registers&1) ^(registers >> 3)) & 1
  registers= (registers >> 1) | (xorValue << 3)
  return registers


#Loop through the length of the plaintext in binary
#Create a keystream from the 4th bit in every cycle
#of the registers.  Don't forget that you must
#include bit 4 of the seed value as the first bit
#in the keyStream.  To get the last bit out of the registers
#variable you can &1 to it.
def makeKeystream(registers, length):
  keyStream = registers
  keyStream = '' + str(registers &1)

#Use cycle(registers) as well as other code you
  for i in range(length):
    registers = cycle(registers)
    keyStream = keyStream + str(registers &1) 

  return keyStream


#Use to convert a string to binary representation
def toBinary(string):
  res = ''.join('{0:08b}'.format(ord(x), 'b') for x in string)
  return res

#Use to convert a binary string to ascii
def toAscii(bits):

  bytes = bits.bit_length() + 7 // 8 
  binary_array = bits.to_bytes(bytes, "big")
  ascii_text = binary_array.decode()
  return ascii_text



def main():
  #Prompt for seed values: input()
  #Wise students will use the int() function with the base 2
  #For example, int('11111111',2) where the 1s are input from the terminal
  seed = input('What is your seed? (enter 4 bits) \n')
  seed = int(seed, 2)
  
  #Input the plaintext message
  plaintext = input('What is your plaintext? \n')
  plaintext = str(plaintext.replace('?', '')) 
  
  #Convert plaintext message to binary
  #Use the toBinary function
  bPlainText = toBinary(plaintext)
  bPlainText = int(bPlainText, 2) 
  count = len(str(bPlainText))
  
  #Generate a keystream that is the length of our plaintext
  #Use makeKeystream(registers, length)
  mkeyStream = makeKeystream(seed, count)
  mkeyStream = int(mkeyStream, 2) 

  #XOR the Plaintext bits and the Keystream bits
  #Use int(variable,2) to represent the variable in binary value
  #The ^ is the XOR operator in python
  encrypted = bin(bPlainText ^ mkeyStream)
  
  print('Here is your encryption: \n', encrypted)
  #To check your work XOR the Ciphertext and the keystream
  #Use int(variable,2) to represent the variable in binary value
  #The ^ is the XOR operator in python
  deciphered = int(encrypted,2) ^ mkeyStream

  print('Here it is deciphered: \n', bin(deciphered))
  
  #To further check your work convert the bits to ascii using
  #the toAscii() function.
  mDeciphered = toAscii(deciphered)
  print(mDeciphered)


if __name__=="__main__":
  main()
