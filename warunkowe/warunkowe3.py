firstNumber = int(input('podaj pierwszą liczbe: '))
secondNumber = int(input('podaj drugą liczbe: '))
thirdNumber = int(input('podaj trzecią liczbe: '))

if firstNumber > secondNumber:
    if firstNumber > thirdNumber:
        print("największa liczba to:", firstNumber)

    else:
        print("największa liczba to:", thirdNumber)

if secondNumber > firstNumber:
    if secondNumber > thirdNumber:
        print('najwięsza liczba to: ', secondNumber)
    else:
        print('najwięsza liczba to: ', thirdNumber)






# numbers = []
#
# numbers.append(firstNumber)
# numbers.append(secondNumber)
# numbers.append(thirdNumber)
#
# smallest = None
# biggest = None
#
# for i in numbers:
#       if smallest == None or smallest > i:
#         smallest = i
#
# for i in numbers:
#     if biggest == None or biggest < i:
#         biggest = i
#
# print ("najmniejsza liczba to:", smallest)
# print ("największa liczba to:", biggest)