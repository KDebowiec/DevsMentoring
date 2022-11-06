weight = int(input("podaj swoją wagę: "))
height = int(input("podaj swój wzrost: "))
BMI = int(weight) * (int(height))**2

if BMI < 18.5:
    print('masz niedowagę!')
elif BMI >= 18.5 and BMI < 24:
    print('masz normalną wagę!')
elif BMI >=24 and BMI < 26.5:
    print('masz lekką nadwagę!')
elif BMI >= 26.5 and BMI < 30:
    print("masz nadwagę!")
elif BMI >= 30 and BMI < 35:
    print('masz nadwagę i otyłość pierwszego stopnia')
elif BMI >=35 and BMI < 40:
    print('masz nadwagę i otyłość drugiego stopnia!')
elif BMI >= 40:
    print("masz nadwagę i otyłość drugiego stopnia")
    