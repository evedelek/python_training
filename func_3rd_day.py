# get_max függvény, amelynek paraméterül meg lehet adni kettő lebegőpontos számot,
# adja vissza a nagyobbat.

def get_max(a: float, b: float) -> float:
    if a > b:
        return a
    else:
        return b

print("A nagyobb szám: ", get_max(6.5, 9.2))



# print_square függvényt, ami paraméterül kap két egész számot.
# rajzoljon ki egy ekkora téglalapot csillagokból.

def print_square(width: int, height: int) -> None:
    full_row = width * "*"
    print(full_row)
    center_row = "*" + (width-2) * " " + "*"
    print((center_row + "\n") * (height-2) + center_row)
    print(full_row)




print_square(7, 6)

# függvény, amely paraméterül megkapja a szavak listáját, és visszadja ezeket összefűzve,
# de mindegyiket gondolatjel között.

def rep(words):
    result = ""
    for word in words:
        result += "-" + word + "-"
    return result

print(rep(["alma", "körte", "meggy"]))