# Írj egy olyan is_ascending függvényt, mely paraméterül kap
# három egész számot. A függvény True-t ad vissza,
# ha a számok szigorúan növekvő sorrendben vannak.
# Ellenkező esetben visszaad egy False értéket.
# 1, 3, 6 -> True
# 1, 10, 20 -> True
# 1, 1, 1 -> False
# 20, 10, 1 -> False
# 20, 10, 20 -> False

def is_ascending(a: int, b: int, c: int):
    return a < b < c



# Írj egy word_concat függvényt, mely két szót kap
# paraméterként, és visszaadja őket összefűzve úgy,
# hogy a rövidebb legyen elől
# "alma", "korte" -> "almakorte"
# "cseresznye", "meggy" -> "meggycseresznye"


