import random

emo ={
   'r':'🪨️',
   'p':'📃️',
   's':'✂️'
}

options =['r','p','s']
guess =(input('Rock, Papper or scissores? (r/p/s)')).lower()
if guess  not in options:
   print('please enter a valid value (r/p/s)')

c_choice =random.choice(options)
print(f'you choose {emo[guess]}')
print(f'computer choose {emo[c_choice]}')
if guess == 'r' and c_choice == 's':
    print('You win!')
elif guess == 'r' and c_choice == 'p':
    print('Computer wins haha!')

elif guess == 'p' and c_choice == 'r':
        print('You win!')
elif guess == 'p' and c_choice == 's':
        print('Computer wins haha!')

elif guess == 's' and c_choice == 'p':
        print('You win!')
elif guess == 's' and c_choice == 'r':
        print('Computer wins haha!')
      