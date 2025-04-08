import re

class WordIterator:
    """
    An iterator that yields words from a given text paragraph.
    """
    def __init__(self, text: str):
        """
        Initializes the WordIterator with the input text.
        """
        self.text = text
        self.index = 0
        self.words = re.findall(r'\b\w+\b', text)  # Extract words using regex
        self.word_index = 0

    def __iter__(self):
        """
        Returns the iterator object itself (required for iteration).
        """
        return self

    def __next__(self):
        """
        Returns the next word in the text.
        Raises StopIteration when all words have been yielded.
        """
        if self.word_index >= len(self.words):
            raise StopIteration
        else:
            word = self.words[self.word_index]
            self.word_index += 1
            return word

# Sample paragraph
paragraph = "Python is a powerful and versatile programming language."

# Create the iterator
word_iter = WordIterator(paragraph)

# Iterate through the words
for word in word_iter:
    print(word)