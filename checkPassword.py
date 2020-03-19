def checkPass(password):
    isUpper = False
    isLower = False
    isSpecialChar = False
    SpecialCharCounter = 0

    for i in password:
        if i.isupper():
            isUpper = True
        elif i.islower():
            isLower = True
        elif i in string.punctuation:
            SpecialCharCounter += 1
            isSpecialChar = True
    # print(str(isUpper) + " " + str(isLower) + " " + str(isSpecialChar) + " " + str(SpecialCharCounter))
    return isUpper and isLower and isSpecialChar and SpecialCharCounter == 1