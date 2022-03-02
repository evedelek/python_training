print(5 * 6)
print(5 + 6)
print(3 / 2)
print(3 - 2)
print(5 * 6 + 12)
print(1 + 2 * 3)
print((1 + 2) * 3)

print("alma" + "korte") #konkatenálás

# Mi van ha össze akarsz adni egy stringet és egy int-et?
#print("alma" + 11)

# Mi van fordítva?
#print(5 + "alma")

# Mi van ha egy stringből ki akarsz vonni egy másikat
#print("alma" - "korte")

# Mi van ha egy stringet megszorzol egy másik stinggel?
#print("alma" * "korte")

# Mi van, ha egy stringet megszorzol egy int-tel?
print("alma" * 5)

result = 6 * 5 + 2
print(result)

number_of_apples_basket = 5
number_of_basket = 3
number_of_all_apples = number_of_apples_basket * number_of_basket
print(number_of_all_apples)

name = "John Doe"
message = "A name valtozo tipusa" + str(type(name))
print(message)

print("Az almak szama: " + str(5))

six = 6
print(six)

# kiértékelések
print(len("hello"))

#változó: órák száma, hours, értéke először 3
# másik változó: minutes, tartalmazza, hogy - előző változó szorzása 60-al
# üzenet kiírása: Három óra az hány perc?

hours = 3
minutes = hours * 60
# print(str(hours) + " óra az " + str(minutes) + " perc")
message = str(hours)
message = message + " óra az "
message = message + str(minutes)
message = message + " perc"
print(message)

number = 5
print(number)
number = number + 3
print(number)

# hozzatok létre egy word nevű változót, és adjátok neki értékül egy nagyon hosszú szót
# számoljátok ki ennek a hosszát
# A csiga pontosan 5 karakter.

word = "csiga"
print("A " + word + " pontosan " + str(len(word)) + " karakter hosszú.")

fruit = "alma"
print('gyumolcs: "' + fruit + '"')
print("gyumolcs: \"" + fruit + "\"")

print(5 % 2)  # maradék 1
print(5 // 2) # ötben a kettő megvan kétszer



