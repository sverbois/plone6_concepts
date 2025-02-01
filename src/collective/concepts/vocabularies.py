from plone import api
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from .interfaces import ISettings


def vocabulary_from_items(items):
    terms = [SimpleTerm(value=key, token=str(key), title=value) for key, value in items.items()]
    return SimpleVocabulary(terms)


@provider(IVocabularyFactory)
def get_bookpublishers_vocabulary(context):
    book_publishers = api.portal.get_registry_record(
        name="collective.concepts.book_publishers",
        default={},
    )
    return vocabulary_from_items(book_publishers)


AUTHOR_NATIONALITIES = []
