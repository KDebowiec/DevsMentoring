sentence = None
list_ = []
conversed_set = None

sentence = input('wpisz zdanie: ')
x = sentence.split('?')
xx = ' '.join(x)
y = xx.split('?')
yy = ' '.join(y)
z = yy.split('!')
zz = ' '.join(z)
a = zz.split(',')
aa = ' '.join(a)
b = aa.split('.')
bb = ' '.join(b)
c = bb.split(':')
cc = ' '.join(c)
list_ = cc.split(';')


conversed_set = set(list_)

print(f'zdanie ma {len(conversed_set)} unikatowych wyrazów')
print(list_)

print(' '.join(list_))

if len(list_) >= 4:
    print(f'pierwszy wyraz zdania to {list_[0]} a czwarty to {list_[3]}')
else:
    print('zdanie jest zbyt krótkie by podać jego pierwszy i czwarty wyraz')
