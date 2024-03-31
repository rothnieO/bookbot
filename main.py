def main():
    book_name = "Frankenstein"
    book_path = "books/frankenstein.txt"
    book_contents = read_book(book_path)
    book_word_count = count_words(book_contents)
    print(f"{book_name} consists of {book_word_count} words.")


def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())



main()