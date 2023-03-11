"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    '''
    >>> wf = WordFinder("simple.txt")
    4 words read

    >>> wf.random() in ["apple","banana","pear","orange"]
    True

    >>> wf.random() in ["apple","banana","pear","orange"]
    True

    >>> wf.random() in ["cat", "dog", "horse"]
    False
    '''
    def __init__(self, file_path):
        '''Read file and print # of lines/items read'''
        file_content = open(file_path)
        
        self.words = self.parse(file_content)

        print(f"{len(self.words)} words read")

    def parse(self, file_content):
        '''Reads every line/word in a file and returns them in a list'''
        return [word.strip() for word in file_content]
    
    def random(self):
        '''Returns a random line/word from the provided file'''
        return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    '''
    Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    4 words read

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["dog", "cat", "horse"]
    False
    '''
    def parse(self, file_content):
        '''
        Reads every line/word in a file and returns them in a list
        if it is not a blank line and
        if it does not start with "#"
        '''
        return [word.strip() for word in file_content if word.strip() and not word.startswith('#')]