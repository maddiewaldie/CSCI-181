# Madeleine Waldie
# CSCI HW 1 - Problem 2
# Vigenere Cipher, using Python 3
 
# Generates a string of the key that repeats itself for the length of the ciphertext / plaintext
def generateKeyString(string, key):
    key = list(key)
    # If the key length and string length are equal, we don't need to do anything & can just return the key
    if len(string) == len(key):
        return(key)
    else:
        # Loop through the plaintext / ciphertext & repeat key
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    # Return the key as a string
    return("" . join(key))
     
# Uses the given key to encrypt a string using the Vigenere Cipher
def encrypt(plainText, key):
    cipherText = []
    # Generate a key to put side by side with the ciphertext to decrypt it
    keyString = generateKeyString(plainText, key)
    # Loop through the plaintext string
    for i in range(len(plainText)):
        # Add together the position of the plaintext letter and the key string's letter to get the ciphertext letter
        x = (ord(plainText[i]) + ord(keyString[i])) % 26
        x += ord('A')
        # Add the ciphertext letter to the array
        cipherText.append(chr(x))
    # Return the ciphertext as a string
    return("" . join(cipherText))
     
# Uses the given key to decrypt a string using the Vigenere Cipher
def decrypt(cipherText, key):
    plainText = []
    # Generate a key to put side by side with the ciphertext to decrypt it
    keyString = generateKeyString(cipherText, key)
    # Loop through the ciphertext string
    for i in range(len(cipherText)):
        # Subtract the key letter position from the position of the ciphertext to get the plaintext letter
        x = (ord(cipherText[i]) - ord(keyString[i]) + 26) % 26
        x += ord('A')
        # Add the plaintext letter to the array
        plainText.append(chr(x))
    # Return the plaintext as a string
    return("" . join(plainText))

# Function to test encryption & decryption
def testEncryptionAndDecryption(plainText, keyword, testNum):
    # Figure out the ciphertext and plaintext
    cipherText = encrypt(plainText, keyword)
    plainText = decrypt(cipherText, keyword)
    # Print out information about test
    print("Test Number ", testNum)
    print("Cipher Text: ", cipherText)
    print("Plain Text: ", plainText)
     
# Main Code: Test encryption & decryption
if __name__ == "__main__":
    testEncryptionAndDecryption("HELLOWORLD", "COOKIE", 1)
    testEncryptionAndDecryption("THISISTHESECONDPROBLEMFORTHECRYPTOHOMEWORK", "LOVE", 2)
    testEncryptionAndDecryption("SANTACLARAUNIVERSITY", "SCU", 3)
    