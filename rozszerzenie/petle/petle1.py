# Napisz program wydrukowywujący poniższy wzór:
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

i = 1
for i in range(6):
    print('*' * i)
for i in range(6, ):
    print('*' * (10-i))