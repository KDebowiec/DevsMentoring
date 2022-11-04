how_many= int(input('podaj do jakiej potęgi ma liczyć program: '))
number=2
compound = 1
result = 2


while compound <= how_many:
  result = number**compound
  print(result)
  compound+=1
