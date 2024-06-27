# About
### This repository contains a collection of programs I built throughout the duration of my Cyber Security Engineering courses at Iowa State University, contains various implementations of encryption and decryption algorithms - including several exploits for several encryption algorithms, exposing weaknesses in implementation, design, and theoretical collisions. 
---
## Categories

[Block Ciphers](https://github.com/jcgarcii/Cryptography-Algorithms/tree/main?tab=readme-ov-file#block-ciphers)
   - Algorithms
     - Rijndael (AES (Advanced Encryption Standard))
     - Feistel (DES (Data Encryption Standard))
   - Attacks
     - AES: Side-channel attacks
     - DES: Brute-force attacks, Differential cryptanalysis

[Stream Ciphers](https://github.com/jcgarcii/Cryptography-Algorithms/tree/main?tab=readme-ov-file#stream-ciphers)
   - Algorithms
     - RC4
     - Salsa20
     - ChaCha20
   - Attacks
     - RC4: Key scheduling attacks, Biases in the keystream
     - Salsa20: Cryptanalysis attacks
     - ChaCha20: Differential attacks

[Substitution Ciphers](https://github.com/jcgarcii/Cryptography-Algorithms/tree/main?tab=readme-ov-file#substitution-ciphers)
   - Algorithms
     - Caesar Cipher
     - Monoalphabetic Cipher
     - Playfair Cipher
   - Attacks
     - Caesar Cipher: Frequency analysis
     - Monoalphabetic Cipher: Frequency analysis
     - Playfair Cipher: Digraph frequency analysis

[Vigenere Ciphers](https://github.com/jcgarcii/Cryptography-Algorithms/tree/main?tab=readme-ov-file#vigenere-ciphers)
   - Algorithms
     - Vigenere Cipher
   - Attacks
     - Vigenere Cipher: Kasiski examination, Frequency analysis
---
## Block Ciphers

### Background
Block ciphers are a type of symmetric-key cipher that encrypts data in fixed-size blocks. Common examples include AES, DES, and Blowfish.

### Algorithms
- **Rijndael / AES (Advanced Encryption Standard)**
- **Feistel / DES (Data Encryption Standard)**
- **Blowfish**

### Attacks
Each block cipher has known vulnerabilities that can be exploited:
- **AES**: Side-channel attacks
- **DES**: Brute-force attacks, Differential cryptanalysis
- **Blowfish**: Weak key attacks

---
## Stream Ciphers

### Background
Stream ciphers encrypt data one bit or byte at a time. They are typically faster than block ciphers and are used in applications where speed is crucial.

### Algorithms
- **RC4**
- **Salsa20**
- **ChaCha20**

### Attacks
Each stream cipher has known vulnerabilities that can be exploited:
- **RC4**: Key scheduling attacks, Biases in the keystream
- **Salsa20**: Cryptanalysis attacks
- **ChaCha20**: Differential attacks


---
## Substitution Ciphers

### Background
Substitution ciphers replace elements of the plaintext with corresponding elements of ciphertext. They are one of the simplest forms of encryption.

### Algorithms
- **Caesar Cipher**
- **Monoalphabetic Cipher**
- **Playfair Cipher**

### Attacks
Each substitution cipher has known vulnerabilities that can be exploited:
- **Caesar Cipher**: Frequency analysis
- **Monoalphabetic Cipher**: Frequency analysis
- **Playfair Cipher**: Digraph frequency analysis

---
## Vigenere Ciphers

### Background
The Vigenere cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution.

### Algorithms
- **Vigenere Cipher**

### Attacks
The Vigenere cipher has known vulnerabilities that can be exploited:
- **Vigenere Cipher**: Kasiski examination, Frequency analysis

