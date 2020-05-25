import json
import os
import pandas

from Book import Book

ORIGINAL_TEXTES_PATH = r"./textes/"
GENERATED_TEXTES_PATH = r"./generated_json"

def main():
    """Call all the classes
    Returns the data in csv data table converted in json.
    """
    for filename in os.listdir(ORIGINAL_TEXTES_PATH):
        if not filename.endswith(".txt"):
            continue

        book = Book(os.path.join(ORIGINAL_TEXTES_PATH, filename))

        book_analyzed = book.spacy_df_pipe()
        book_json_string = book_analyzed.to_json()

        with open(os.path.join(GENERATED_TEXTES_PATH, f"{filename}.json"), "w") as json_files:
            json_files.write(book_json_string)

if __name__ == "__main__":
    main()