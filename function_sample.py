#is_even nevű függvény,amely true-t ad vissza, ha paraméterként megadott érték páros , egyéb esetben false

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(7))

# Szorgalmi
# Hozz létre egy sum_negatives függvényt, mely paraméterül kap egy listát,
# és összegzi a benne szereplő negatív számokat, és azzal tér vissza

def sum_negatives(numbers):
    sum_n = 0
    for i in numbers:
        if i < 0:
            sum_n += i
    return sum_n

list_of_numbers = [1, 3, -1, -10, -7, 3]
print(sum_negatives(list_of_numbers))



# Szorgalmi
# Hozz létre egy to_minutes függvényt, mely paraméterül megkapja
# az órák számát, és visszatér a percek számával
def to_minutes(hours):
    return hours*60
print(to_minutes(6))

# Szorgalmi
# Hozz létre egy input_number függvényt, melynek legyen egy
# paramétere. A függvény bekér a felhasználótól egy szöveget
# a paraméterrel megadott szöveggel, számmá konvertálja és azt adja vissza
def input_number(message):
    return int(message)

value = input_number("Adj meg egy számot!")
print(type(value))


# Szorgalmi
# Írjatok egy annotate_every_even_number függvényt, mely kap egy
# számok listáját, és kiírja őket egymás alá, de minden másodikat
# egy karakterrel beljebb ír ki

def annotate_every_even_number(numbers):
    counter = 1
    for numbers in numbers:
        if is_even(counter):
            print(" " + str(number))
        else:
            print(number)
            counter +=1
        even_number = not even_number

annotate_every_even_number([1, 4, 5, 7, 9, 11])



# Feladat 5
# Írj egy concatenate_shorts függvényt, mely paraméterül kap szavak listáját
# és csak a 3 karakternél rövidebb szavakat fűzze össze egy stringbe,
# és ezt adja vissza
def concatenate_shorts(words):
    result = ""
    for word in words:
        result =result + word
    return result

print(concatenate_shorts(["manó, bogyó, esernyő"]))