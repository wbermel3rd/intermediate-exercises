myList = [1,2,3,4,3,2,5,1,7,5,6]

def get_unique_list(inList):
    output = []
    for x in inList:
        if(x not in output):
            output.append(x)
    return output
unique_list = get_unique_list(myList)
print(unique_list)