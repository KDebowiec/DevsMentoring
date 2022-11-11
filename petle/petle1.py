question = 'Podaj do ilu mam policzyć: '
how_many= int(input('podaj do ilu mam policzyć: '))
number=0


while number <= how_many:
  print(number)
  number+=1


how_many= int(input(question))


for number in range(how_many):
  print(number)