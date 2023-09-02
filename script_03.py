myWord = (input('Enter a string: '))

def count_letters(inWord):
    output = {}
    inWord = inWord.lower()
    for x in inWord:
        if x != ' ':
            if(x not in output.keys()):
                output.update({x:1})
            else:
                output.update({x:output.get(x) + 1})
    return output

toPrint = count_letters(myWord)
print(toPrint)