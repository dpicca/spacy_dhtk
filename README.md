# Spacy DHTK  

## Introduction  

Spacy is a Python parser for books. The code uses spaCy, a free open-source library for Natural Language Processing in Python. It is used to analyse texts by using linguistic features thanks to the NLP (Natural Language Processing). 
This project was realised during the class “Object Oriented Programming in Python” teached by Davide Picca and assisted by Coline Métrailler.  

University of Lausanne – Spring 2020

The database is based on 50 English books in plain text format (.txt) from the Project Gutenberg website : http://www.gutenberg.org/.  

The generated JSON scripts are located in the generated_json folder.  

## Dependencies
- Python 3

## Usage 


The full pipeline that is used to generate the JSON file is found in the `main.py` script. 

## Data 
The book analyzor return data that is converted into JSON format applying the `???`method.

## Book 
The class book corresponds to the parsed book. 
The method `get_name()` returns the name of the book then `get_lines()` divides the text in lines.


## Character 
The class character corresponds to the characters from the book. 

The `spacy_characters()` method allows access to the list of characters and context of the apparition. 

## Line
The class line corresponds to the separation in paragraphs using spaCy’s NLP. 


