
print("Gondolj egy számra 1-10 között!")
min = 1
max = 10
answer = "x"
while answer != "e":
    guess = int((min + max) // 2)
    print("A tippem", guess)
    answer = input("nagyobb [n], kisebb [k], egyenlő [e]")
    if answer == "k":
        max = guess - 1
    elif answer == "n":
        min = guess + 1
print(" A gondolt szám", guess)