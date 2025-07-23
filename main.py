from stats import get_num_words
from stats import get_book_text
from stats import char_counter
from stats import sort_dict
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]
text = get_book_text(path)
words = get_num_words(text)
char = char_counter(text)
word_counter = sort_dict(char)

print("=============== BOOKBOT ===============")
print(f"Analyzing book found at {path}...")
print("--------------- Word Count-------------")
print(f"Found {words} total words")
print("--------------- Character Count--------")
for item in word_counter:
    for key, value in item.items():
        print(f"{key}: {value}")