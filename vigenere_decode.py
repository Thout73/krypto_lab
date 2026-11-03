import sys
import math


def ggT(array):
    current = 0
    for elem in array:
        if current == 0:
            current = elem
        else:
            current = math.gcd(current, elem)
    return current

inputpath = sys.argv[1]
inputfile = open(inputpath,'r')
message = inputfile.read()

characters = "abcdefghijklmnopqrstuvwxyz"

characters = characters.upper()
message = message.upper()

indexes = dict()

formated_message = ""

for char in message:
    if char in characters:
        formated_message += char

n = len(formated_message)

for i in range(1,100):
    ic = 0
    for k in range(0, i):
        occ = [0] * 26
        j = k
        while j < n:
            occ[characters.find(formated_message[j])] += 1
            j += i
        part_ic = 0
        for elem in occ:
            part_ic += elem * (elem - 1)
        part_ic = part_ic / (sum(occ) * (sum(occ) - 1))
        ic += part_ic
    ic = ic / i
    indexes[i] = ic

possible_key_lengths = []
for key in indexes:
    if indexes[key] > 0.07:
        possible_key_lengths.append(key)

key_length = ggT(possible_key_lengths)

# now count again and pick highest as e
key = ""
for i in range(0, key_length):
    occ = [0] * 26
    j = i
    while j < n:
        occ[characters.find(formated_message[j])] += 1
        j += key_length
    key += characters[(occ.index(max(occ)) - 5) % 26]
    
print("Der Schlüssel ist ", key)
decoded_message = ""

key_index = 0
for char in message:
    if char in characters:
        pos = characters.find(char)
        new_pos = (pos - characters.find(key[key_index]) - 1) % len(characters)
        key_index = (key_index + 1)% len(key)
        decoded_message += characters[new_pos]
    else:
        decoded_message += char


outputpath = sys.argv[2]
outputfile = open(outputpath, 'w')
outputfile.write(decoded_message)
print("Entschlüsselung erfolgreich!")
