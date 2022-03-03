# bekérés: hány számot szeretne megadni?
# 3
# kérjél be tőle pont annyit számot, mint amennyit az előbb megadott
# összegezzük a felhasználó által megadott csak pozitív számokat


sum = 0
count = int(input("Hány számot szeretnél megadni?"))
for i in range(count):
        number = int(input("Add meg a " + str(i +1) + " számot"))
        print("A megadott szám:", number)
        if number > 0:
        sum =+ number
        print("A szamok osszege", sum)