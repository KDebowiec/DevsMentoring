# Zakładając, że masz dostęp do adresu w formacie: username@companyname.com,
# napisz program, który wydrukuje nazwę firmy z takiego adresu.
# Zarówno nazwa użytkownika jak i nazwa firma może składać się tylko i wyłącznie z liter.
import re


text = 'username@companyname.com'

match = re.sub("([a-zA-Z0-9\\_\\-\\.]+)@([a-zA-Z]+).(.+)", r'\2', text)
print(match)