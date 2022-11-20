# Zapisz wszystkie wyrazy z poniższego tekstu do słownika (jako klucze). Wartości
# przypisane do tych kluczy mają być równe ilości wystąpień słowa w tekście.
#
# "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint "
# "and curious volume of forgotten lore, While I nodded, nearly napping, suddenly there "
# "came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor,"
# " I muttered, tapping at my chamber door - Only this, and nothing more."
import re
a_list = []
text_dictionary = {}
text = 'Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint ' \
       'and curious volume of forgotten lore, While I nodded, nearly napping, suddenly there' \
       'came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor,' \
       'I muttered, tapping at my chamber door - Only this, and nothing more.'
new_text = re.sub(r"[^a-zA-Z0-9 ]","", text)

a_list = new_text.split()


for i in a_list:
    text_dictionary.update({i : a_list.count(i)})

print(text_dictionary)