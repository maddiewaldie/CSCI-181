def DecimalToBinary(number, n):
    """
     DecimalToBinary(int number, int n), with two integer inputs number and n
     This function takes an integer number and converts it to a binary array of length n.
     Its output is an array of length n giving the binary representation of number. 
     So DecimalToBinary(100, 8) should output [0,1,1,0,0,1,0,0].
    """
    # Convert number to binary string
    binary_string = bin(number)[2:]
    # Pad with leading zeros to make sure the binary string is of length n
    padded_binary_string = binary_string.zfill(n)
    # Convert the binary string to an array of integers
    binary_array = [int(bit) for bit in padded_binary_string]
    return binary_array

def ConvertBitArraytoInt(k, n):
    """
    ConvertBitArraytoInt(Array k, int n)
    This function takes an array of bits and converts every n bits to its decimal representation.
    So ConvertBitArraytoInt([1,0,0,0,0,0,1,1,1,0,0,1], 3) should output [4, 0, 7, 1]. 
    This will be used to convert the secret key input to RC4 to its decimal equivalent to be used in the RC4 algorithm
    """
    # Split the input array into chunks of length n
    chunks = [k[i:i+n] for i in range(0, len(k), n)]
    # Convert each chunk to its decimal representation
    decimals = [int(''.join(map(str, chunk)), 2) for chunk in chunks]
    return decimals


def RC4(n, l, key):
    """
    This function generates the RC4 keystream based on the input parameters.
    """
    # Initialize S and T arrays
    S = list(range(256))
    T = [key[i % len(key)] for i in range(256)]
    j = 0
    # Initial permutation of S array
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]
    # Generate keystream
    keystream = []
    i = j = 0
    for _ in range(n * l):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        keystream.append(S[t])
    return keystream

# Test DecimalToBinary
print("DecimalToBinary Test:", DecimalToBinary(100, 8), "\n") # DecimalToBinary(100, 8) should output [0,1,1,0,0,1,0,0]

# Test ConvertBitArraytoInt
print("ConvertBitArrayToInt Test", ConvertBitArraytoInt([1,0,0,0,0,0,1,1,1,0,0,1], 3), "\n") # ConvertBitArraytoInt([1,0,0,0,0,0,1,1,1,0,0,1], 3) should output [4, 0, 7, 1]. 

# Question 1 b:
n = 3
l = len("BACDDAH")
key = DecimalToBinary(1236, 4)
keystream = RC4(n, l, ConvertBitArraytoInt(key, 8))
plaintext = "BACDDAH"
plaintext_bits = []
for char in plaintext:
    plaintext_bits.extend(DecimalToBinary(ord(char), 8))
ciphertext_bits = [plaintext_bits[i] ^ keystream[i] for i in range(n * l)]
print("Keystream:", keystream)
print("Plaintext bits:", plaintext_bits)
print("Ciphertext bits:", ciphertext_bits, "\n")

# Question 1 c:
n2 = 8
l2 = 24
key2 = [1, 0, 1, 1, 1, 0, 0, 1 , 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1]
keystream2 = RC4(n2, l2, ConvertBitArraytoInt(key2, 24))
print("Keystream:", keystream2, "\n")

# Question 1 d:
key3=[1, 0, 1, 1, 1, 0, 0, 1 , 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1,
1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,
0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1,
1, 0, 1, 0, 0, 0, 1]
ciphertext3= [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0,
0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0,
0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0,
0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1,
0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0,
1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1,
1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0]
def repeat_key(key, n):
    repeated_key = key * (n // len(key)) + key[:n % len(key)]
    return repeated_key
key4 = repeat_key(key3, len(ciphertext3))
plaintext3 = [key4[i] ^ ciphertext3[i] for i in range(n2 * l2)]
