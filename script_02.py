dict1 = {'a':5, 'b':7, 'c':2, 'd':13}
dict2 = {'b':2, 'c':8, 'd':-2, 'e':17}

def get_combined_dict(inDict1, inDict2):
    output = {}
    for x in inDict1:
        if(inDict2.get(x) != None):
            output.update({x: (inDict1.get(x) + inDict2.get(x))})
    return output
combined_dict = get_combined_dict(dict1, dict2)
print(combined_dict)

