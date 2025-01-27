from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


def vocabulary_from_items(items):
    terms = [SimpleTerm(value=key, token=str(key), title=value) for key, value in items.items()]
    return SimpleVocabulary(terms)


BOOK_CATEGORIES = {
    "pol": "Roman policier",
    "scf": "Science fiction",
    "his": "Histoire",
}


@provider(IVocabularyFactory)
def get_bookcategories_vocabulary(context):
    return vocabulary_from_items(BOOK_CATEGORIES)


AUTHOR_NATIONALITIES = []
