import json

inputfile = 'output.txt' #enter compressed file name here!

#inport huffman tree dictionary
dictionary = open('dictionary.json', 'r')
input_dict = json.load(dictionary)

compressedFile = inputfile = open(inputfile, 'r', encoding = "utf-8").readlines()
bytelist = []
binarylist = []
for line in inputfile:
    for char in line:
        bytelist.append(format(ord(char),'08b'))
for byte in bytelist:
    for char in byte:
        binarylist.append(char)
        

dictionaryValues = list(input_dict.values())
dictionaryKeys =  list(input_dict.keys())
character = []
charList = []
for char in binarylist:
    character.append(str(char))
    for value in dictionaryValues:
        if character == value:
            n = dictionaryKeys[dictionaryValues.index(value)]
            charList.append(n)
            character = []
            break
output = ''.join(charList)
outputTextfile = open('Decompressed.txt','w', encoding="utf-8")
outputTextfile.writelines(output)
    
    