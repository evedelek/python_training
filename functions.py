def print_emp_data(name, age):
    print("Az alkalmazott neve:", name)
    print("Az alkalmazott kora:", age)

print_emp_data("john", 10)
print_emp_data("jack", 20)
print_emp_data("jane", 30)
print('end')


def print_dog_name(name):
    print ("A kutya neve", name)
print_dog_name("Néro")

# két darab számot vár, és a konzol kiírja az összegüket
# kéjétek be a függvényen kívül a két számot és a bekért értékekkel hívjátok meg a print_sum függvényt.
def print_sum(a, b):
    print(a+b)
print_sum(4, 9)


#Írjatok egy sum_list függvényt, ami paraméterül kap egy listát, és kiírja a konzolra a listában szereplő számok összegét.

numbers = [1, 2, 5, 8]

def sum_list(numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)










