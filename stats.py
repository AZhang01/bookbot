def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()
        return file_content
    
def get_num_words(text):
    return(len(text.split()))

def char_counter(words):
    lower_case = words.lower()
    letter_counter = {}
    for char in lower_case:
        letter_counter[char] =  letter_counter.get(char,0)+1

    return letter_counter

def sort_on(items):
    for value in items.values():
        return value

def sort_dict(dict):
    dict_list = [{k:v} for k, v in dict.items() if k.isalpha()]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    