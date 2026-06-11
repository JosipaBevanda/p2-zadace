"""
Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.
"""
def brojevi(n):
    print("Parni:")
    for i in range(n):
        if i % 2 == 0:
            yield i

    print("Neparni:")
    for i in range(n):
        if i % 2 != 0:
            yield i

gen = brojevi(10)

for broj in gen:
    print(broj)
