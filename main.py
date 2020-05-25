import json
import os
import pandas

from Book import Book

ORIGINAL_TEXTES_PATH = "./textes"
GENERATED_TEXTES_PATH = "./generated_json"

def main():

    for filename in os.listdir(ORIGINAL_TEXTES_PATH):
        if not filename.endswith(".txt"):
            continue

        book = Book(filename)
        book_analyzed = book.spacy_char_pipe()

        with open(os.path.join(GENERATED_TEXTES_PATH, filename[:-4] + ".json"), "w") as json_script:
			json_script.dumps(book_analyzed, indent=4)



if __name__ == "__main__":
    main()

