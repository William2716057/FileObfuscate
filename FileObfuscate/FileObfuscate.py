
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
inputFile = "filename"
outputFile = "hex.txt"
toHex(inputFile, outputFile)

#take hex.txt and perform vigenere, save as encrypted.txt
def vigenereEncrypt(plaintext, key):
    encrypted = ''
    keyIndex = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[keyIndex % len(key)].lower()) - ord('a')
            if char.islower():
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            keyIndex += 1
        else:
            encrypted += char
    return encrypted

def encryptFile(inputFile2, outputFile2, key):
    try:
        with open(inputFile2, 'r') as f:
            plaintext = f.read()
            
        encryptedText = vigenereEncrypt(plaintext, key)
        
        with open(outputFile2, 'w') as f:
            f.write(encryptedText)
        
        print("Encryption complete. Saved to", outputFile2)
    except FileNotFoundError:
        print("File not found")

inputFile2 = "hex.txt"
outputFile2 = "encrypted.txt"
key = input("Enter encryption key: ")


encryptFile(inputFile2, outputFile2, key)

#take encrypted.txt and decode to decoded.txt
def decryptFile(inputFile3, outputFile, key):
    try:
        with open(inputFile3, 'r') as f:
            encryptedText = f.read()

        decryptedText = vigenereDecrypt(encryptedText, key)

        with open(outputFile, 'w') as f:
            f.write(decryptedText)

        print("Decryption complete. Saved to", outputFile)
    except FileNotFoundError:
        print("File not found")

def vigenereDecrypt(ciphertext, key):
    decryptedText = ""
    keyLength = len(key)
    keyIndex = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[keyIndex % keyLength].lower()) - ord('a')
            if char.isupper():
                decryptedText += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                decryptedText += chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            keyIndex += 1
        else:
            decryptedText += char
    return decryptedText


inputFile3 = "encrypted.txt"
outputFile = "decrypted.txt"
key = input("Enter decryption key: ")
decryptFile(inputFile3, outputFile, key)


#take decoded.txt and recompile as recompiled.'filetype'

def hexRecompile(inputFile4, outputFile3):
    try:
        with open(inputFile4, 'r') as f:
            hex_data = f.read().strip()

        if len(hex_data) % 2 != 0:
            raise ValueError("Invalid hex data length")

        originalData = bytes.fromhex(hex_data)

        with open(outputFile3, 'wb') as f:
            f.write(originalData)

        print("Recompiled file saved to", outputFile3)

    except FileNotFoundError:
        print("File not found.")
    except ValueError as e:
        print("Error:", e)
        
inputFile4 = "decrypted.txt"
outputFile3 = "recompiled" #user must add correct extension

hexRecompile(inputFile4, outputFile3)