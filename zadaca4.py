"""
Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje kao prvo slovo vašeg imena, 
a završava kao prvo slovo prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak.
"""

import re

regex = r"^J(?=.*[0-5])(?=.* ).*B$"

tekst = "Josipa 3B"

if re.match(regex, tekst):
    print("Podudara se")
else:
    print("Ne podudara se")

