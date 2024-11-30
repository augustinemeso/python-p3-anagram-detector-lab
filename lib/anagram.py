# anagram.py
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Store word in lowercase to ensure case insensitivity

    def match(self, possible_anagrams):
        matches = []
        for possible_word in possible_anagrams:
            if sorted(self.word) == sorted(possible_word.lower()):
                matches.append(possible_word)
        return matches


# Test the Anagram class when the script is run directly
if __name__ == "__main__":
    listen = Anagram("listen")
    
    # Testing the match method with a list of possible anagrams
    result = listen.match(['enlists', 'google', 'inlets', 'banana'])
    print(result)  # Expected output: ['inlets']
