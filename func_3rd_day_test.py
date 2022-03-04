# teszt eset = python függvény
from func_3rd_day import get_max

def test_get_max():
    # given: bemeneti adatok
    a =5
    b = 10
    # when: megkapjuk az aktuális értéket
    result = get_max(a, b)
    #then
    assert result == 10


def test_get_max_when_first_value_ist_greater():
    assert get_max(200, 5) == 200
