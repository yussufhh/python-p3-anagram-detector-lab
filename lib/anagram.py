# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  

    def match(self, word_list):
        sorted_word = sorted(self.word) 
        matches = []
        
        for candidate in word_list:
            if sorted_word == sorted(candidate.lower()):  
                matches.append(candidate)
        
        return matches
