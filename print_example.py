print("alma", end="")
print("korte", end="")

#Hozz letre egy last_functions.py állományt, ebben egy
# table függvényt, ami kiírja a szorzótáblát!
def table():
    for i in range(1,11):
        for j in range(1, 11):
            print(i * j, end=" ")
        print("")
table()


# Hozz létre egy digits függvényt, ami kiírja a
# paraméterül adott szám számjegyeit!

def digits(numbers):
    for i in str(numbers):
        print(i)

digits(1683)