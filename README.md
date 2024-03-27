
A simple Python script that performs file obfuscation and deobfuscation using hex data of files and the Vigenere Cipher. 
This is performed using several functions to achieve each step

Read the file in binary mode ('rb').

Input file is converted into hexadecimal format.
The hexadecimal code is written to hex.txt.

Encrypt Hexadecimal File using Vigenere Cipher:

The hexadecimal file is read and encrypted using a VIgenere Cipher with a key input by the user.
The encrypted contents are stored as encrypted.txt

Decrypt Encrypted File:

The contents of encrypted.txt are read 
The contents of encrypted.txt are decoded if correct key is input by user.
The file is saved as decrypted.txt.

Recompile Decrypted File:

Contents of decrypted.txt are read
The function converts the contents of decrypted.txt back into it's original form and saves as recompiled.
The user must add correct extension type to make file usable.
