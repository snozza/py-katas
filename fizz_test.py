def test_dividable_by_3_is_fizz():
    num = 6
    assert is_fizz(num) is True

def test_not_dividable_by_3_is_not_fizz():
    num = 2
    assert is_fizz(num) is False

def test_dividable_by_5_is_buzz():
    num = 10 
    assert is_buzz(num) is True

def test_not_dividable_by_5_is_not_buzz():
    num = 9
    assert is_buzz(num) is False

def test_dividable_by_5_and_3_is_fizzbuzz():
    num = 15
    assert is_fizz_buzz(num) is True

def test_fizz_buzz_is_fizz():
    num = 6
    assert fizz_buzz(num) is 'fizz'

def test_fizz_buzz_is_buzz():
    num = 20
    assert 'buzz' if is_buzz(fizz_buzz(num)) else num is 'buzz'

def is_fizz(num):
    return (num % 3 == 0)

def is_buzz(num):
    return (num % 5 == 0)

def is_fizz_buzz(num):
    return is_fizz(num) and is_buzz(num)

def fizz_buzz(num):
    return 'fizz' if is_fizz(num) else num
