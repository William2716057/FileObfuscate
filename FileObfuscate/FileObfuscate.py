
#take file and save as hex.txt

def toHex(inputFile, outputFile):
    try:
        with open(inputFile, 'rb') as f:
            hexdump = f.read().hex()
            
        with open (outputFile, 'w') as f:
            f.write(hexdump)
            
        print("saved to ", outputFile)
    except FileNotFoundError:
        print("File not found")
        
#inputFile = input("enter path to file: ")
inputFile = "sandwich.png"
outputFile = "hex.txt"
toHex(inputFile, outputFile)

#take hex.txt and perform vigenere, save as encrypted.txt
def vigenereEncrypt(plaintext, key):
    encrypted = ''
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            if char.islower():
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            encrypted += char
    return encrypted

def encryptFile(inputFile2, outputFile2, key):
    try:
        with open(inputFile2, 'r') as f:
            plaintext = f.read()
            
        encrypted_text = vigenereEncrypt(plaintext, key)
        
        with open(outputFile2, 'w') as f:
            f.write(encrypted_text)
        
        print("Encryption complete. Saved to", outputFile2)
    except FileNotFoundError:
        print("File not found")

inputFile2 = "hex.txt"
outputFile2 = "encrypted.txt"
key = input("Enter encryption key: ")

#toHex(inputFile, outputFile)
encryptFile(inputFile2, outputFile2, key)
#take encrypted.txt and decode to decoded.txt
#take decoded.txt and recompile as recompiled.'filetype'