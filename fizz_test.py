def test_dividable_by_3_is_fizz():
    num = 6
    assert is_fizz(num) is True

def test_not_dividable_by_3_is_not_fizz():
    num = 2
    assert is_fizz(num) is False

def test_dividable_by_5_is_buzz():
    num = 10 
    assert 10 is True

def is_fizz(num):
    return True if (num % 3) == 0 else False 
