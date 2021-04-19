import random

def GenerateContents(lowcount = 5, uppercount = 5, numcount = 11):
    LowerAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    UpperAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    
    with open("lowerchars.txt", "w") as file:
        file.truncate()
        for i in range(1, lowcount): 
            file.writelines(random.choice(LowerAlphabet))

    with open("upperchars.txt", "w") as file:
        file.truncate()
        for i in range(1, uppercount): 
            file.writelines(random.choice(UpperAlphabet))

    with open("NumberGen.txt", "w") as file:
        file.truncate()
        for i in range(1, numcount): 
            file.writelines(str(random.randint(0, 9)))



def CreatePassword():
    with open("lowerchars.txt", "r") as file:
        lowerlist = file.readlines()
        lower = ''.join([str(lowerlist) for lowerlist in lowerlist])

    with open("upperchars.txt", "r") as file:
        upperlist = file.readlines()
        upper = ''.join([str(upperlist) for upperlist in upperlist])

    with open("NumberGen.txt", "r") as file:
        numlist = file.readlines()
        num = ''.join([str(numlist) for numlist in numlist])


    before = lowerlist+upperlist+numlist #have a list
    shuffleOne = random.sample(before, len(before)) #shuffle one time
    shuffleTwo = random.sample(shuffleOne, len(shuffleOne)) #shuffle second time
    finalpass = ''.join([str(shuffleTwo) for shuffleTwo in shuffleTwo]) # make into string
    return print(finalpass) #final password
    
GenerateContents(7, 7, 7) # index values are for how many lowercase letters, uppercase letters, and numbers will be in the password, respectively. 
CreatePassword()