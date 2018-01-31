from collections import Counter

def test_is_anagram():
    word1 = 'hello'
    word2 = 'hlleo'
    assert (count_items(word1) == count_items(word2)) is True

def count_items(sequence):
    return Counter(sequence)

