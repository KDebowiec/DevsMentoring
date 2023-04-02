# Wykorzystując paradygmat funkcyjny oraz metodę count(), sprawdź ile ciągów nie zawiera w sobie napisu składającego się z dwóch 1 obok siebie.
#
lines = ['10000101011', '111111', '01010101010010', '011001100001', '001010101011']


nums = list(filter(lambda x: x.count('11') >0, lines))

print(nums)