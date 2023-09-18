# Madeleine Waldie
# CSCI HW 4 - Problems 3-5
# SHA3, using Python 3

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

# Grab input array from provided text file
with open('sha3in.txt', 'r') as f:
    v = list(map(int, f.read().strip()))
a = inputSHA3(v) # turn 1d array into 3d array
aout = theta(a) # apply the theta function

# Test theta function
print("aout[4][3][9:18] = ", "".join(map(str, aout[4][3][9:19])))
print("aout[3][1][15:24] = ", "".join(map(str, aout[3][1][15:25])))

