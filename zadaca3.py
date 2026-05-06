"""
Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata ime.prezimeX@sum.ba 
X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo ime.prezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
"""

import re

email_regex = r"^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$"
eduid_regex = r"^[a-zA-Z]+\.[a-zA-Z]+[0-9]*@sum\.ba$"

email = input("Unesi e-mail: ")
eduid = input("Unesi eduId: ")

if re.fullmatch(email_regex, email):
    print("E-mail je ispravan.")
else:
    print("E-mail nije ispravan.")

if re.fullmatch(eduid_regex, eduid):
    print("eduId je ispravan.")
else:
    print("eduId nije ispravan.")
