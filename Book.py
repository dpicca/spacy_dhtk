#Insérer votre code ici
#Classe principale Book
from dataclasses import dataclass
import pandas
import spacy
from tqdm import tqdm
import json
from Line import Line
from Character import Character

@dataclass
class Book:
    """
    General Book class
    """
    path:str
    def get_name(self):
        """
        Returns the book's name situated in the path
        
        Returns
        -------
        name: str
            a string of the name of the book
        
        Example
        -------
        ::
        
            test = Book(book_path)
            bookName = test.get_name()
        """
        name = self.path.split('/')[-1]
        name = name.split('.')[0]
        return name
    def get_lines(self):
        """
        Parse the lines in a file

        Returns
        -------
        lines: str
            lines parsed into a list

        """
        with open(self.path, 'r', encoding='utf-8', newline='\n') as file:
            content = file.read()
            lines = content.split('\n')
            return lines
    def spacy_ner(self):
        """
        Prepares the text for spacy's NER annotation scheme

        Returns
        -------
        paragraphs: table
            separated paragraphs of the book
        len_diffs : table
            integer of difference of length

        """
        paragraphs = []
        len_diffs = []
        for line in tqdm(self.get_lines()):
            line_length = len(line)
            paragraph = Line.spacy_tag(line) 
            len_diff = line_length - len(paragraph.text)
            paragraphs.append(paragraph)
            len_diffs.append(len_diff) 
        return paragraphs, len_diffs

    def spacy_char_pipe(self):
        """
        Creates a .json file containing each appearance of each character

        Returns
        -------
        characters_sorted: list
            list of characters sorted by number of occurences
        context: list
            list of occurences of each character

        """
        name = self.get_name()
        
        paragraphs, _ = self.spacy_ner()
        test = Character(paragraphs)
        characters_sorted, context = test.spacy_characters(paragraphs)
        json_char = {'counter': characters_sorted, 'context': str(context)}
            
        with open(f'./Data/{name}_characters_spacy.json', 'w', encoding='utf-8') as file:
            json.dump(json_char, file)
                    
        return characters_sorted, context

    def spacy_pos_tagging(self):
        """
        Apply Spacy's POS tagging system to each word of a book.
        
        Returns
        -------
        tagging_df: csv
            tagged entities
        """
        entities = []
        offset = 0
        
        paragraphs, len_diffs = self.spacy_ner()
        
        for i in range(len(paragraphs)):
            paragraph = paragraphs[i]
            len_diff = len_diffs[i]
            for token in paragraph:

                entity = {
                    'name': token.text,
                    'lemma': token.lemma_,
                    'Type': token.pos_,
                    'Tag': token.tag_,
                    'Shape': token.shape_,
                    'Alpha' : token.is_alpha,
                    'Stop' : token.is_stop,
                }

                entities.append(entity)

            offset += len(paragraph.text) + len_diff + 1

        tagging_df = pandas.DataFrame(entities)

        name = self.get_name()
        tagging_df.to_csv(f'./Data/{name}_spacy.csv')
        
        return tagging_df

    def spacy_get_dependencies(self):
        """
        Returns a list of the dependencies between words in a book
        
        Returns
        -------
        dependency_df: csv
            list of all dependencies
        """
        entities = []
        offset = 0
        
        paragraphs, len_diffs = self.spacy_ner()
        
        for i in range(len(paragraphs)):
            paragraph = paragraphs[i]
            len_diff = len_diffs[i]
            for token in paragraph.noun_chunks:
                entity = {
                    'Text': token.text,
                    'Main Noun': token.root.text,
                    'Dependency': token.root.dep_,
                    'Main Noun Object': token.root.head.text,
                }

                entities.append(entity)

            offset += len(paragraph.text) + len_diff + 1

        dependency_df = pandas.DataFrame(entities)

        name = self.get_name()
        dependency_df.to_csv(f'./Data/{name}_spacy.csv')
        
        return dependency_df

    def spacy_df_pipe(self):
        """
        Creates a .csv file containing a five column dataframe containing Spacy entities
        
        Returns
        -------
        entity_df: csv
            five column dataframe tale
        """
        entities = []
        offset = 0
        
        paragraphs, len_diffs = self.spacy_ner()
        
        for i in range(len(paragraphs)):
            paragraph = paragraphs[i]
            len_diff = len_diffs[i]
            for ent in paragraph.ents:

                entity = {
                    'name': ent.text, 
                    'start_pos': offset + ent.start_char, 
                    'end_pos': offset + ent.end_char, 
                    'tag': ent.label_, 
                    'score': 1, 
                }

                entities.append(entity)

            offset += len(paragraph.text) + len_diff + 1

        entity_df = pandas.DataFrame(entities)

        name = self.get_name()
        entity_df.to_csv(f'./Data/{name}_spacy.csv')
        
        return entity_df

