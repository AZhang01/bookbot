def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()
        return file_content
def get_num_words(text):
    return(len(text.split()))