import string
import random


while True:
    charLength = int(input('Desired length of password:'));
    puncLength = int(input('Desired number of punctuation:'));
    capLetLength = int(input('Desired number of capital letters:'));
    numLength = int(input('Desired number of digits:'));

    totalDesiredCharacters = puncLength + capLetLength + numLength;

    if (totalDesiredCharacters <= charLength):
        break;
    else:
        print("Desired character sum and character length don't equal to each other")

punc = []
caps = []
nums = []

password = []

for x in range(0,puncLength):
    password.append(random.choice(string.punctuation));

for x in range(0,capLetLength):
    password.append(random.choice(string.ascii_uppercase));


for x in range(0,numLength):
    password.append(random.choice(string.digits));

numCharLeft = charLength - puncLength - capLetLength - numLength;

for x in range(0,numCharLeft):
    password.append(random.choice(string.ascii_lowercase));

random.shuffle(password);

new_password = " ";
for char in password:
    new_password += char;

print(new_password)