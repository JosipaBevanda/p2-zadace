"""
Napisati rekurzivnu funkciju koja kao parametar prima string, a kao rezultat taj string ispisuje sa zada.
"""
def ispis_unatrag(tekst):
    if tekst == "":
        return
    print(tekst[-1], end="")
    ispis_unatrag(tekst[:-1])

