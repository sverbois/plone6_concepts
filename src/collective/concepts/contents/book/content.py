from plone import schema
from plone.app.dexterity import textindexer
from plone.app.textfield import RichText
from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.indexer import indexer
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from z3c.form.browser.radio import RadioFieldWidget
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope.interface import implementer


class IBook(model.Schema):
    """Book interface"""

    # Fields
    category = schema.Choice(
        title="Category",
        vocabulary="collective.taxonomy.bookcategories",
        required=True,
    )

    publisher = schema.Choice(
        title="Publisher",
        vocabulary="collective.concepts.BookPublishers",
        required=False,
    )

    isbn = schema.TextLine(
        title="ISBN",
    )
    cover = NamedBlobImage(
        title="Image de couverture",
        required=False,
    )
    back = RichText(
        title="4ème de couverture",
        max_length=2000,
        required=False,
    )
    price = schema.Decimal(
        title="Prix du livre",
        required=False,
    )
    authors = RelationList(
        title="Auteurs",
        default=[],
        value_type=RelationChoice(
            title="Auteur",
            vocabulary=StaticCatalogVocabulary(
                {
                    "portal_type": ["Author"],
                },
                title_template="{brain.Type}: {brain.Title} at {path}",
            ),
        ),
        required=False,
    )

    # Searcheable
    textindexer.searchable("isbn")

    # Widgets
    directives.widget("authors", SelectFieldWidget)
    # directives.widget(
    #     "authors",
    #     AjaxSelectFieldWidget,
    #     pattern_options={  # Some options for Select2
    #         "minimumInputLength": 2,  # Don't query until at least two characters have been typed
    #         "ajax": {"quietMillis": 500},  # Wait 500ms after typing to make query
    #     },
    # )


@indexer(IBook)
def book_category_indexer(object):
    return object.category


@implementer(IBook)
class Book(Container):
    """Book content type"""
