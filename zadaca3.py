"""
Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.
Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena. 
Nedovoljan
0-49%
Dovoljan
50-65%
Dobar
65-80%
Vrlodobar
80-90%
Izvrstan
90-100%
"""
imena = ["Ivan", "Ana", "Marko"]
prezimena = ["Ivic", "Anic", "Markic"]
godine = [20, 19, 21]
postotci = [45, 78, 92]

studenti = list(zip(imena, prezimena, godine, postotci))

# sortiranje po prezimenu (drugi element tuplea)
studenti.sort(key=lambda student: student[1])

print("Sortirana lista po prezimenima:")
for student in studenti:
    print(student)

rangovi = {
    "Nedovoljan": 0,
    "Dovoljan": 0,
    "Dobar": 0,
    "Vrlodobar": 0,
    "Izvrstan": 0
}

for student in studenti:
    postotak = student[3]

    if postotak < 50:
        rangovi["Nedovoljan"] += 1
    elif postotak <= 65:
        rangovi["Dovoljan"] += 1
    elif postotak <= 80:
        rangovi["Dobar"] += 1
    elif postotak <= 90:
        rangovi["Vrlodobar"] += 1
    else:
        rangovi["Izvrstan"] += 1

print("\nBroj ostvarenih ocjena:")
for rang in rangovi:
    print(rang, ":", rangovi[rang])