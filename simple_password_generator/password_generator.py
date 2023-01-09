import random

def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)

upperCase1 = chr(random.randint(65,90))
upperCase2 = chr(random.randint(65,90))
lowerCase1 = chr(random.randint(97,122))
lowerCase2 = chr(random.randint(97,122))
digit1 = random.randint(0,9)
digit2 = random.randint(0,9)

password = upperCase1 + upperCase2 + lowerCase1 + lowerCase2 + str(digit1) + str(digit2)

print(password)

password = shuffle(password)

print(password)