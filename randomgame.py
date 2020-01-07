import random

random_num = random.randint(1, 10)
print(random_num)
while True:
    answer = input('Guess a number between 1 and 10: ')
    if int(answer) == random_num:
        print('you are right!')
        break
    else:
        print('Try again')
