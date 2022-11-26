sentence = input('wpisz zdanie: ')
forbidden_signs = ['?', '!', ',', '.', ':', ';']

for i in forbidden_signs:
    sentence.replace(i, ' ')

list_ = sentence.split(' ')

converted_set = set(list_)

print(f'zdanie ma {len(converted_set)} unikatowych wyrazów')
print(list_)

print(' '.join(list_))

if len(list_) >= 4:
    print(f'pierwszy wyraz zdania to {list_[0]} a czwarty to {list_[3]}')
else:
    print('zdanie jest zbyt krótkie by podać jego pierwszy i czwarty wyraz')
