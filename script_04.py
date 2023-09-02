numSum = 0
for x in range(1, 6):
    while(True):
        userIn = input('Enter int #' + str(x) + ': ')
        try: 
            temp = int(userIn)
            break
        except ValueError: 
            print('Invalid input. Please enter an int.')
    numSum += temp

print('Your sum is ' + str(numSum))
        
    
    