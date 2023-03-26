# Bazując na następującym tekście:
# “The quick brown fox jumps over the lazy dog is an English-language pangram—a sentence that contains all of the letters
# of the English alphabet”, wydziel go na listę przechowującą długości kolejnych wyrazów z pominięciem słowa “the”, np.
#
# length_of_words = [5, 5, 3, 5, ...], co odpowiada kolejno długościom wyrazów: quick, brown, fox, jumps.
text = 'The quick brown fox jumps over the lazy dog is an English-language pangram—a sentence ' \
       'that contains all of the letters of the English alphabet'

forbidden_signs = ['?', '!', ',', '.', ':', ';', '-', 'The']

for i in forbidden_signs:
    text.replace(i, ' ')
list_ = text.split(' ')

length_of_words = [len(i) for i in list_]
print(length_of_words)