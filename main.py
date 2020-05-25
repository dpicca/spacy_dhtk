import json 
import os 

from Book import Book

ORIGINAL_TEXTES_PATH = "./textes"
GENERATED_TEXTES_PATH = "./generated_json"

def main():

    book_analyzor = Book()

    for filename in os.listdir(ORIGINAL_TEXTES_PATH):
        if not filename.endswith(".txt"):
            continue

        with open(os.path.join(GENERATED_TEXTES_PATH, filename), 'r', encoding='utf-8') as file:
            content = file.read()
        
        book = book_analyzor.???

if __name__ == "__main__":
    main()

