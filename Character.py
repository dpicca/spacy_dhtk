#Classe Character
@dataclass
# Determine if the entity is a person
class Character:

  def __init__(self, paragraphs):
    """
    Init function of a Character
    """
    self.paragraphs = paragraphs

  def is_char(self, entity):
    """
    Checks whether an entity, like a word, is tagged as a character
    
    Returns
    -------
    entity.label: bool
        Boolean value
    """
    return entity.label == 'PERSON'

  def count_char(self, paragraph):
    """
    Counts the amount of characters in a given paragraph
    
    Returns
    -------
    nb_char_par: int
        integer value of the number of characters
    
    """
    nb_char_par = Counter()

    for entity in paragraph.ents:
      if self.is_char(entity):
        nb_char_par[entity.text] += 1

    return nb_char_par

  def sort_char(self, char_list):
    """
    Sort a list of characters by from most to least common
    
    Returns
    -------
    characters_sorted: list
        list of characters sorted by frequency
    """
    characters_sorted = char_list.most_common()
    return characters_sorted

  def spacy_characters(self, paragraphs):
    """
    Returns the occurencies of characters in each paragraph
    
    Returns
    -------
    characters_sorted: dict
        Characters and their number of appearances per paragraph
    context: dict
        Dictionary of characters paired with a list of paragraphs they appear in
    """
    nb_characters = Counter()
    context = defaultdict(list)

    for paragraph in paragraphs:
      nb_char_par = self.count_char(paragraph)
      nb_characters.update(nb_char_par)
      for entity in nb_char_par:
        context[entity].append(paragraph)

    characters_sorted = self.sort_char(nb_characters)
    return characters_sorted, context