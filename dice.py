import random

while True:
    print(random.randint(1,6))
    again = input('Do you want to role the dice again? (y/n):')
    if again.lower() == 'y':
        continue
    else:
        break


print('Bye!')