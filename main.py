def main():
    book_name = "Frankenstein"
    book_path = "books/frankenstein.txt"
    book_contents = read_book(book_path)                            # entire book text
    book_word_count = len(book_contents.split())                    # count of words
    book_letter_count_dict = count_letters(book_contents)           # dictionary of all symbols with counts
    book_letter_count_list = create_list(book_letter_count_dict)    # list of dictionaries, alpha symbols only
    book_letter_count_list_sorted = sort_list(book_letter_count_list)

    print(f"{book_name} consists of {book_word_count} words.")
    for entry in book_letter_count_list_sorted:
        char = entry["char"]
        count = entry["count"]
        print(f"{char} appears {count} times")
   


def sort_list(list):
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(dict):
    return dict["count"]

def create_list(dict):
    list = []
    for char in dict:
        if char.isalpha():
            list.append({"char":char,"count":dict[char]})
    return list


def read_book(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    count_letters_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in count_letters_dict:
            count_letters_dict[char] += 1
        else:
            count_letters_dict[char] = 1
    return count_letters_dict




main()