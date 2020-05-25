# Spacy DHTK  

## Introduction  

Spacy is a Python parser for books. This project was realised during the class “Object Oriented Programming in Python” teached by Davide Picca and assisted by Coline Métrailler.  

The code was written by : Jason Ola, Gislain Delavy, Victor Vermot-Petit- Outhenin and Caroline Roxana Rohrbach.

University of Lausanne – Spring 2020

The database is based on 50 English books in plain text format (.txt) from the Project Gutenberg website : http://www.gutenberg.org/.  

The generated JSON scripts are located in the generated_json folder.  

## Dependencies
- Python 3

## Objective 

The objective of the project is to work with texts from Gutenberg.org, using spaCy, a free open-source library for Natural Language Processing (NLP) in Python. It is used to analyse texts by using linguistic features thanks to the NLP.

To do so, three dataclasses were created : 
`Book`, `Character` ,`Line`.

The dataclass `Book` corresponds to the parsed book.

The dataclass `Character` corresponds to the characters from the book. 

The dataclass `Line` corresponds to the tagging of paragraphs using spaCy’s NLP.

The code to generate the JSON file can be found in the `main.py`script. 

## Procedure 
The first step of the creation of this code was the division of the three data classes below. Then we created the methods which are the following : 
`Book`:
The method `get_name()` returns the name of the book then `get_lines()` divides the text in lines.
The three following methods return a Dataframe and creates a csv file with an array of the information : 
`spacy_pos_tagging()`separate the text in entities. 
`spacy_get_dependencies()`is a method that uses the NLP of the text and uses the dependencies between the words in a book. 
`spacy_df_pipe()` is a method that return spacy entities.
`Character`
The method `spacy_characters()` allows access to a dictionary of characters and the number of occurrence in the text.


## Results 
The results can be found in a JSON file in the `main.py` script.  The data are separated in an array and takes the arguments that are in the `spacy_df_pipe()` method. 

All of this information can be found in the `generated_json` file.  

Here is a screenshot of a generated dataframe : 

![DataFrame](images/df_example.png)