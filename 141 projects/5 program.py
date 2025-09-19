#wite program to generate random numbers, random alphabets and random characters

import random
import string

#for random number 0 -100
print (f"random number :{random.randint(0,100)}")

#for random lowercase alphabet
random_lower = random.choice(string.ascii_lowercase)
print (f"random lowercase alphabet : {random_lower}")

#for random uppercase alphabet
random_upper = random.choice(string.ascii_uppercase)
print(f"random uppercase :{random_upper}")

#for random special character
random_char = random.choice(string.punctuation)
print(f"special random character:  {random_char}")


#for random combined random 
char = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
random_combined = ''.join(random.choice(char) for i in range(12))
print(f"random combined : {random_combined}")