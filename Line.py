# spacy_tag dans une autre classe qu'on appele depuis spacy_ner dans la classe Book !
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
