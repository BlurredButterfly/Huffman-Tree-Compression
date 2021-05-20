import json

textfile = "input.txt" #Enter input file name here
inputfile = open(textfile, 'r', encoding = 'utf-8').readlines()


#Main function used to execute the program
def main(inputfile)-> None:
    huffmanTree = createHuffmanTree(inputfile)
    dictionary = createDictionary(inputfile, huffmanTree)
    compressContent(inputfile, dictionary)
    with open('dictionary.json','w') as file:
        file.write(json.dumps(dictionary))

def createHuffmanTree(inputfile)->list: 
    output = countFrequency(inputfile)
    orderedList = sortContent(output)
    huffmanTree = createNodes(orderedList)
    return(huffmanTree)
    print(huffmanTree)

#Counts the frequency of characters in a textfile.
def countFrequency(textfile)-> list:
    content = {}
    for line in textfile:
        for char in line:
            if char in content:
                content[char] += 1
            else:
                content[char] = 1
    output = list(map(list, content.items()))
    return(output)

#Sorts the list of characters made by CountFrequency() into most frequent first.
def sortContent(content)->list:
    functionInput = content
    output = []
    for i in range(len(content)):
        highestValue=0
        highestElementIndex=0
        for j in range(len(functionInput)):
            element = functionInput[j]
            if element[1] > highestValue:
                highestValue = element[1]
                highestElementIndex = j
        output.append(functionInput[highestElementIndex])
        functionInput.pop(highestElementIndex)
    return(output)

#Adds a node into a list of nodes at the correct position.
def insertNode(content, node)->list:
    output = content
    value = node[1]
    for element in content:
        if element[1] < value:
            output.insert((output.index(element)),node)
            break
    return(output)

#Creates nodes for a Huffman Tree from an ordered list of characters and character frequencies
def createNodes(content)->list:
    output = content
    if len(output)==2:
        return(output)
    else:
        nodeArray =[]
        nodeArray.append(output[len(output)-1])
        nodeArray.append(output[len(output)-2])
        x = nodeArray[0]
        y = nodeArray[1]
        nodeValue = x[1] + y[1]
        node = [nodeArray, nodeValue]
        functionInput = content
        functionInput.pop(len(content)-1)
        functionInput.pop(len(content)-1)
        output = insertNode(functionInput, node)
        output = createNodes(output)
    return(output)

#Compressed as input textfile according to an input Huffman tree
def compressContent(inputfile, dictionary)-> list:
    binaryList=[]
    byte = []
    chars = []
    output=[]
    for line in inputfile:
        #every character in inputfile checked.
        for char in line:
            dictionaryKeys = dictionary.keys()
            #checks dictionary for character
            for item in dictionaryKeys:
                if item == char:
                    binaryList.append(dictionary[char])
                    break
        percentage = "Compression " + str((inputfile.index(line)/len(inputfile))*100) + "% complete"
        print(percentage)
    for code in binaryList:
        for item in code:
            if len(byte) == 7:
                byte.append(item)
                chars.append(byte)
                byte = []
            else:
                if code == binaryList[len(binaryList)-1]:
                    if item == code[len(code)-1]:
                        while len(byte) < 8:
                            byte.append('0')
                else:
                    byte.append(item)
        
    for item in chars:
        binaryString= ""
        binaryString = int(binaryString.join(item),2)
        char = chr(binaryString)
        output.append(char)
    outputTextfile = open('output.txt','w', encoding="utf-8")
    outputTextfile.writelines(output)
    print('compression complete')


#Finds the binary representation of a character according to a HuffmanTree      
def findCode(hoffmanTree, char)->list:
    code=[]
    for item in hoffmanTree:
        if type(hoffmanTree[1]) is list:
            if type(item[0]) is list:
                code = findCode(item, char)
            elif str(item[0]) == str(char):
                if item == hoffmanTree[0]:
                    code.append('0')
                else:
                    code.append('1')
                break
            if code != []:
                if type(hoffmanTree[1]) is list:
                    if item == hoffmanTree[0]:
                        code.insert(0,'0')
                    else:
                        code.insert(0,'1')
                break
        else:
            code = findCode(hoffmanTree[0], char)
    return(code)

def createDictionary(inputfile, huffmanTree)->dict:
    characterList = countFrequency(inputfile)
    orderedList = sortContent(characterList)
    dictionary = {}
    for item in orderedList:
        char = item[0]
        dictionary[char] = tuple(findCode(huffmanTree, char))
        percentage = int((orderedList.index(item)/len(orderedList))*100)
        print("Dictionary " + str(percentage) + "% complete")
    return(dictionary)


main(inputfile)