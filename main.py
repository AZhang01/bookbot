def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()
        word_count = file_content.split()
        return len(word_count)

text = get_book_text("./books/frankenstein.txt")
print(text, "words found in the document")
