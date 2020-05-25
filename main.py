import json
import os
import pandas

from Book import Book

ORIGINAL_TEXTES_PATH = "./"
GENERATED_TEXTES_PATH = "./generated_json"

def main():

    for filename in os.listdir(ORIGINAL_TEXTES_PATH):
        if not filename.endswith(".txt"):
            continue

        book = Book(os.path.join(ORIGINAL_TEXTES_PATH, filename))

        book_analyzed = book.spacy_char_pipe()
        book_json = json.loads(book_analyzed.to_json())
        book_json_string = json.dumps(book_json, indent=4)

        with open(os.path.join(GENERATED_TEXTES_PATH, f"{filename}.json"), "w") as json_files:
            json_files.write(book_json_string)





if __name__ == "__main__":
    main()