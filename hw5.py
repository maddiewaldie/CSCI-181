# Madeleine Waldie
# CSCI HW5
# SHA3, using Python 3

import numpy as np

# Implement a function called inputSHA3() that turns a 1-dimensional array of length 1600, 
# v[0 . . . 1599], to a 3-dimensional array a[0 . . . 4][0 . . . 4][0 . . . 63] such that a[i][j][k] = v[64(5j + i) + k].
def inputSHA3(v):
    a = [[[0 for k in range(64)] for j in range(5)] for i in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(64):
                a[i][j][k] = v[64*(5*j+i)+k] # formula from  homework sheet
    return a

# Implement a function called outputSHA3() that turns a 3-dimensional array a[0 . . . 4][0 . . . 4][0 . . . 63] 
# into a 1-dimensional array of length 1600, v[0 . . . 1599], such
# that v[64(5j + i) + k] = a[i][j][k].
def outputSHA3(a):
    v = [0 for i in range(1600)]
    for i in range(5):
        for j in range(5):
            for k in range(64):
                v[64*(5*j+i)+k] = a[i][j][k] # formula from homework sheet
    return v

# Implement the function θ from a 3-dimensional array ain[0 . . . 4][0 . . . 4][0 . . . 63] to a 3-dimensional array 
# aout[0 . . . 4][0 . . . 4][0 . . . 63]. To check your work, apply your function to the input file provided and the output 
# aout[4][3][9 . . . 18] should be 0011011000. Apply θ to the input file provided. In your homework writeup, list the ten bits 
# aout[3][1][15 . . . 24].
def theta(ain):
    aout = [[[0 for k in range(64)] for j in range(5)] for i in range(5)]
    xor1 = [[[0 for k in range(64)] for j in range(5)] for i in range(5)]
    xor2 = [[[0 for k in range(64)] for j in range(5)] for i in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(64):
                for x in range(5):
                    xor1[i][j][k] = ain[(i-1)%5][x][k]
                    xor2[i][j][k] = ain[(i+1)%5][x][k]
                aout[i][j][k] = ain[i][j][k] ^ xor1[i][j][k] ^ xor2[i][j][k]
    return aout


# Implement the function ρ from a 3-dimensional array ain[0...4][0...4][0...63] to a 3-dimensional array 
# aout[0...4][0...4][0...63]. Note that the rho matrix is: 
# rhomatrix=[0,36,3,41,18;1,44,10,45,2;62,6,43,15,61;28,55,25,21,56;27,20,39,8,14]. 
# To check your work, apply your function to the input file provided to you, the output 
# aout[4][3][9 . . . 18] should be 0110011001. Apply ρ to the input file provided. In your homework writeup, 
# list the ten bits aout[3][1][15 . . . 24].
def rho(ain):
    rhomatrix = [[0,36,3,41,18],[1,44,10,45,2],[62,6,43,15,61],[28,55,25,21,56],[27,20,39,8,14]]
    rhom = np.array(rhomatrix, dtype=int)
    aout = [[[0 for _ in range(64)] for _ in range(5)] for _ in range(5)]

    for i in range(5):
        for j in range(5):
            for k in range(64):
                aout[i][j][k] = ain[i][j][k - rhom[i][j]]
    return aout

# Implement the function π from a 3-dimensional array ain[0...4][0...4][0...63] to a 3-dimensional 
# array aout[0...4][0...4][0...63]. To check your work, apply your function to the input file provided 
# and the output aout[4][3][9...18] should be 0110110001. Apply π to the input file provided. In your 
# homework writeup, list the ten bits aout[3][1][15 . . . 24].
def pi(ain):
    a_out = [[[0 for _ in range(64)] for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(64):
                a_out[j][(2*i+3*j)%5][k] = ain[i][j][k]
    return a_out

# Implement the function χ from a 3-dimensional array ain[0...4][0...4][0...63] to a 3-dimensional array 
# aout[0...4][0...4][0...63]. To check your work, apply your function to the input file provided (sha3in.txt) 
# and the output aout[4][3][9 . . . 18] should be 0110100001. Apply χ to the input file provided. In your homework writeup, 
# write down the ten bits aout[3][1][15 . . . 24].
def chi(ain):
    aout = [[[0 for _ in range(64)] for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(64):
                a = ain[i][j][k]
                b = (ain[(i+1)%5][j][k] ^ 1) % 2
                c = ain[(i+2)%5][j][k]
                aout[i][j][k] = (a ^ (b & c))
    return aout

# Implement the function χ from a 3-dimensional array ain[0...4][0...4][0...63] to a 3-dimensional array 
# aout[0...4][0...4][0...63]. To check your work, apply your function to the input file provided 
# (sha3in.txt) and the output aout[4][3][9 . . . 18] should be 0110100001. Apply χ to the input file provided. 
# In your homework writeup, write down the ten bits aout[3][1][15 . . . 24].

with open('sha3in.txt', 'r') as f:
    a = list(map(int, f.read().strip()))

ain = inputSHA3(a) # turn 1d array into 3d array

print("rho step:")
aout1 = rho(ain)
print(aout1[3][1][15:25])

print("rho check:")
aout12 = rho(ain)
print(aout12[4][3][9:19])

print("\npi step:")
aout2 = pi(ain)
print(aout2[3][1][15:24])

print("\npi check:")
aout22 = pi(ain)
print(aout22[4][3][9:19])

print("\nchi step:")
aout3 = chi(ain)
print(aout3[3][1][15:24])

print("\nchi check:")
aout32 = chi(ain)
print(aout32[4][3][9:19])