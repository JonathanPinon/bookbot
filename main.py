def main():
    book_path = "books/frankenstein.txt"
    book_text = read_book(book_path)
    num_words = calculate_num_words(book_text)
    char_counter = count_characters(book_text)
    book_data = character_data(char_counter, num_words)
    # print(char_counter)
    print(book_data)
    # print(num_words)


def read_book(path):
    with open(path) as f:
        return f.read()


def calculate_num_words(book_text):
    words = book_text.split()
    return len(words)


def count_characters(book_text):
    counter = {}
    text_to_lower = book_text.lower()
    for i in text_to_lower:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1
    return counter


def character_data(char_counter, num_words):
    print("-- Begin report of Frankenstein.txt --")
    print(f"{num_words} words found in the document")
    for key in char_counter:
        if key.isalpha() is True:
            print(f"The '{key}' character was found {char_counter[key]} times")
    return "-- End Report --"


main()
