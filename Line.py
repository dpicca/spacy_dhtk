# spacy_tag dans une autre classe qu'on appele depuis spacy_ner dans la classe Book !
from dataclasses import dataclass
import spacy
import en_core_web_lg
nlp = spacy.load("en_core_web_lg")

@dataclass
class Line:
  def spacy_tag(self):
    """
    Tags a paragraph using Spacy's NLP
    
    Returns
    -------
    paragraph: str
        paragraph of the book, tagged
    """
    paragraph = nlp(self)
    return paragraph
