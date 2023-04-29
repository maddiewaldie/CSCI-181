# Madeleine Waldie
# CSCI HW 1 - Problem 3
# Vigenere Cipher Histograms, using Python 3
import string

# Ciphertext to analyze
ciphertext = "lpiusnwkwcyiezwwcqelxdeizabhvthgwbkjrcfshevgiwxetnxfesgasgxeibgwmldzrewkfrrtbkmirhngveirorwvhqqsaxslzdvnlavixpqmgpbhvrbluyqxvglayxrqxjzlragalayqxbhcmbhsgawkuvnhlltmievksgxkeibfzjhvuthlnkioxlmyugytafvhgnnkxcwanlykuvwltfwqdrgxvpydvgagnakefygknkegmzxjdwfbfznkiexztxzseglaypvrtdesdfbnlmbhwnfwthgfbmzmbdxzhjgcqkrjmtfocytqbhoinowlhrwgxhaugxehvwyqfytudikmxxhmnkisbjlnisetfhnkiewsrshxxggpcqkuhopubprtvliqxbpsrcgshulxxljvlzhoohrowkwrqrusvelwutdevhxredbhjxubkpcwlnlazbvszxoayuinzwluqhnzwlbhrpxlpiusnwkwcyiezwwcqejhgwuqhvmghewlrhfxfhwfmjtphprwtruqhgasmbdwztvxuopgawwcijrkwgwhve"
ciphertext = ciphertext.upper()
key_length = 7

# Loop through the ciphertext by the keylenhth increments & count letter frequency
for i in range(key_length):
    freqs = [0] * 26
    for j in range(i, len(ciphertext), key_length):
        if ciphertext[j] in string.ascii_uppercase:
            freqs[ord(ciphertext[j]) - ord('A')] += 1
    print(f"{freqs}\n")