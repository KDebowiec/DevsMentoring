sentence = None
list_ = []
conversed_set = None

sentence = input('wpisz zdanie: ')
list_ = sentence.split()

conversed_set = set(list_)

print(f'zdanie ma {len(conversed_set)}unikatowych wyrazów')
print(list_)

for element in conversed_set:
    print(element, end = ' ')

print(f'pierwszy wyraz zdania to {list_(0)} a czwarty to {list_(3)}')
