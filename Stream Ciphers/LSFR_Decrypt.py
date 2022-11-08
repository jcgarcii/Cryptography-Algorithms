# Lab 05 Part 02 
from base64 import encode
import binascii
import math
import sys


#The cycle function produces the new bit, shifts the registers to the right by one position,
#and puts the new bit in the 4th bit position.
#As it is written it XORs the first bit and the last bit in the registers
#You may need to select different bits to create the correct xorValue
#However, the shifting of the registers will not need to be modified.
def cycle(registers):
  xorValue = ((registers&1) ^ (registers << 1)) & 1
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
  bits = int(bits, 2)
  bytes = bits.bit_length() + 7 // 8 
  binary_array = bits.to_bytes(bytes, "big")
  ascii_text = binary_array.decode(errors='ignore')
  return ascii_text

#Gives user the Suspected Keystream:
def knownText(plaintext, ciphertext):
  #Convert plaintext message to binary
  #Use the toBinary function
  bPlainText = toBinary(plaintext)
  count = len(bPlainText)
  bPlainText = int(bPlainText, 2) 
  #Gathers the first n-bits:
  bCiphertext = ciphertext[0:count]
  #XOR the Plaintext over the first few bits 
  bCiphertext = int(bCiphertext, 2)
  print('Here is the plain ', bPlainText)
  print('Here is cipher', bCiphertext)

  suspected = format(bPlainText ^ bCiphertext, 'b') 

  #Present the User with the Suspected Keystream: 
  print('Here is your suspected keysteam: ')
  print(suspected)

  keyLen = input('What is your suspected period? ')
  keyLen = int(keyLen)

  degree(keyLen)

  ##print('Use this on your spreadsheet: ',suspected[0:keyLen])

#calculates the degree of the LFSR: 
def degree(i):

  degree = math.log2(i + 1)
  
  print('Here is your period: ', i)
  print('Here is your degree: ', degree)
  

def solve(ciphertext):
  #Collect the suspected Seed from the Previous Portion:
  seed = input('What is your suspected seed? \n')
  seed = int(seed, 2)
  
  #Ciphertext:
  count = len(ciphertext)
  ciphertext = int(ciphertext, 2)
  #Use makeKeystream(registers, length)
  mkeyStream = makeKeystream(seed, count)
  mkeyStream = int(mkeyStream, 2) 
  #XOR the Plaintext bits and the Keystream bits
  #Use int(variable,2) to represent the variable in binary value
  #The ^ is the XOR operator in python

  deciphered = format(ciphertext ^ mkeyStream, 'b')
  print('Here it is: ', deciphered)
  #print('Here it is deciphered: \n', bin(deciphered))
  #To further check your work convert the bits to ascii using
  #the toAscii() function.
  #
  #print('Here it is ', deciphered)

  mDeciphered = toAscii(deciphered)
  print(mDeciphered)


def main():
  #initiate the suspected keystream process
  #Prompt for known plaintext: 
  plaintext = input('What is your known plaintext? \n')
  #Prompt for the ciphertext: 
  ciphertext = input('What is the ciphertext? \n')
  knownText(plaintext, ciphertext)
  #solve:
  solve(ciphertext)


if __name__=="__main__":
  main()
