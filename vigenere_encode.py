import sys

inputpath = sys.argv[1]
inputfile = open(inputpath,'r')
message = inputfile.read()
key = sys.argv[2]

characters = "abcdefghijklmnopqrstuvwxyz"

characters = characters.upper()
message = message.upper()
key = key.upper()

encoded_message = ""


key_index = 0
for char in message:
    if char in characters:
        pos = characters.find(char) + 1
        new_pos = (pos + characters.find(key[key_index])) % len(characters)
        key_index += 1
        key_index = key_index % len(key)
        encoded_message += characters[new_pos]
    else:
        encoded_message += char

outputpath = sys.argv[3]
outputfile = open(outputpath, 'w')
outputfile.write(encoded_message)
print("Verschlüsselung erfolgreich!")