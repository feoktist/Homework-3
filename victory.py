import random

questions = {'Alex': '01.01.2019', 'Bob': '02.02.2019', 'Charlie': '03.03.2019', 'Dave': '04.04.2019', 'Evan': '05.05.2019',
             'Frank': '06.06.2019', 'Gregory': '07.07.2019', 'Helen': '08.08.2019', 'Ian': '09.09.2019', 'John': '10.10.2019'}

people = questions.keys()



say = input("Shall we play? ")

while say not in {'n', 'N'}:
  random_people = random.sample(people, 5)
  counter = 0
  errors = 0
  for k in random_people:
      
    
    answer = input(f'Enter dd.mm.yyyy for writher {k}: ')
    if answer == questions[k]:
      print('Correct!')
      print('\n')
      counter += 1
      
      
    else:
      print('Wrong!')
      print('The right answer is: ', questions[k])
      print('\n')
      errors += 1
      

  print('\n')
  print(' =============== RESULTS ================')
  print('Correct answers: ', counter)  
  print('Wrong answers: ', errors)  
  print(' =========================================')

    
  say = input("Shall we play again? (y/n): ")

print('\n')
print('Bye!')
print('\n')
print('End of program')
