#név, ha üres, akkor írjuk ki , hogy nem lehet üres értéket megadni
#kérjük be újra
#ha nem ürs, írjuk ki, hogy köszönöm


name = ""
while name == "":
    name = input("Add meg a neved: ")
    if name == "":
        print("Nem jó, nem adhatsz meg üres értéket!")
print("Köszönöm!")