# testing/anagram_test.py
from anagram import Anagram

def test_anagram():
    listen = Anagram("listen")
    
    # Test with valid anagrams
    result = listen.match(['enlists', 'google', 'inlets', 'banana'])
    assert result == ['inlets']
    
    # Test with no matches
    result = listen.match(['dog', 'mouse', 'banana'])
    assert result == []

    # Test with the word itself in the list
    result = listen.match(['listen', 'inlets', 'banana'])
    assert result == ['listen', 'inlets']
