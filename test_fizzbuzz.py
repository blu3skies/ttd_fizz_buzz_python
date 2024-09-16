from fizzbuzz import fizzbuzz

def test_fizzbuzz_1():
    assert fizzbuzz(2) == [1, 2]

def test_fizzbuzz_fizz():
    assert fizzbuzz(3) == [1, 2, "Fizz"]
