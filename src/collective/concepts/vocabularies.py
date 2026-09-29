from plone import api
from zope.component import getUtility
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


def vocabulary_from_items(items):
    terms = [SimpleTerm(value=key, token=str(key), title=value) for key, value in items.items()]
    return SimpleVocabulary(terms)


def get_title_from_vocabulary_value(vocabulary_name, vocabulary_value):
    factory = getUtility(IVocabularyFactory, vocabulary_name)
    vocabulary = factory(None)
    try:
        term = vocabulary.getTerm(vocabulary_value)
        return term.title
    except:
        return vocabulary_value


@provider(IVocabularyFactory)
def get_bookpublishers_vocabulary(context):
    book_publishers = api.portal.get_registry_record(
        name="collective.concepts.book_publishers",
        default={},
    )
    return vocabulary_from_items(book_publishers)
