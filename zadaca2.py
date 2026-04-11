"""
Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu
od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1)
"""
import random
imena = ["Miro", "Stjepan", "Josip", "Toni", "Robert", "Marko", "Ljubo",
         "Josipa", "Magdalena", "Ivana", "Stipe", "Emanuel", "Petar",
         "Ivan", "Luka", "Filip", "Lara", "Laura", "Mario", "Ana", "Marija",
         "Nikolina", "Andrija", "Slaven", "Sebastian", "Marko", "Frano",
         "Stipan", "Eugen", "Toni", "Dražan", "Matej", "Nives", "Nemanja",
         "Sara", "Ružica", "Gabrijel", "Darian", "Ivana", "Ivan Stjepan",
         "Kristian", "Josip", "Tomislav", "Jovan", "Gabrijel", "Mia", "Ante",
         "Josip", "Ante", "Josip", "Danijel", "Goran", "Zoran Ivan",
         "Franjo Francisko", "Sergej", "Matej", "Marin", "Sara", "Josip",
         "Stjepan", "Iva", "Marko", "Sara", "Krešimir", "Magdalena", "Marko",
         "Mirko", "David", "Ema", "Paul", "Sven", "Natalija", "Petar",
         "Emanuel", "Helena", "Antonio", "Petar"]

ocjene = {}
for ime in imena: 
    ocjene[ime] = random.randint(1, 5)

# brojanje ocjena
brojac = {1:0, 2:0, 3:0, 4:0, 5:0}
for ocjena in ocjene.values():
    brojac[ocjena] += 1

# prolaznost
ukupno = len(ocjene)
prolazni = 0
for o in ocjene.values():
    if o > 1:
        prolazni += 1

postotak = prolazni / ukupno * 100

# ispis
print("Ocjene po studentima:")
for ime in ocjene:
    print(ime, ocjene[ime])

print("Broj ocjena:", brojac)
print("Postotak prolaznosti:", postotak)