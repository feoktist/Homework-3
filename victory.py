import random

questions = {'a': '01.01.2019', 'b': '02.02.2019', 'c': '03.03.2019', 'd': '04.04.2019', 'e': '05.05.2019',
             'f': '06.06.2019', 'g': '07.07.2019', 'h': '08.08.2019', 'i': '09.09.2019', 'j': '10.10.2019'}

people = questions.keys()

say = input("Shall we play? ")

while say not in {'n', 'N'}:
    random_people = random.sample(people, 5)
    counter = 0
    errors = 0
    print('\n')
    print('Guess bdays of these guys: ', mix)
    print('\n')

    for writer in writers:
        print('----------------------------------')
        print('Guess the dd.mm.yyyy for: ', writer)
        print('\n')
        answer = (input('your answer: '))
        if answer in writers.values():
            print('you guessed it right!')
            counter = + 1
        else:
            print('wrong!')
            print('the right answer is: ', writer.values())
            errors = + 1

    print('Correct answers: ', counter)
    print('Wrong answers: ', errors)

    say = input("Shall we play again? (y/n): ")

print('\n')
print('Bye!')
print('\n')
print('End of program')




