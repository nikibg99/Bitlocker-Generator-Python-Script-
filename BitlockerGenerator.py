import random

bit = random.randrange(100000,999999,6)
converted = str(bit)
f = open('bitlocker.txt', 'w') 
f.write(converted)