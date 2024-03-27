
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
#take encrypted.txt and decode to decoded.txt
#take decoded.txt and recompile as recompiled.'filetype'