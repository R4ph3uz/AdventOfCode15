StartNumber = input("Please enter your starting number:  ")
CurrentNumber = StartNumber

for x in range (10):
    Length = len(CurrentNumber)
    NewNumber = ""
    i = 0
    while True:
        for j in range (i, Length):
            if CurrentNumber[i] != CurrentNumber[j]:        
                break
#        if j == 0:
        NewNumber = NewNumber + str(j + 1) + CurrentNumber[i]
#        else:
#            NewNumber = NewNumber + str(j) + CurrentNumber[i]
        i += max(1, j)
        if i >= Length - 1:
            break

    CurrentNumber = NewNumber
    print(CurrentNumber)