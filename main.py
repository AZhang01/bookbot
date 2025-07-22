from stats import get_num_words
from stats import get_book_text
from stats import char_counter

text = get_book_text("./books/frankenstein.txt")
words = get_num_words(text)
char = char_counter(text)

print(char)
