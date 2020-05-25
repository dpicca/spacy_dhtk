import json
import os


from Book import Book

ORIGINAL_TEXTES_PATH = "./textes"
GENERATED_TEXTES_PATH = "./generated_json"

def main():

    for filename in os.listdir(ORIGINAL_TEXTES_PATH):
        if not filename.endswith(".txt"):
            continue

        book = Book(filename)
        book_analyzed = book.spacy_char_pipe()
        


if __name__ == "__main__":
    main()

