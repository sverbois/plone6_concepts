from zope import schema
from zope.interface import Interface


class IBrowserLayer(Interface):
    """Browser layer marker interface"""


class ISettings(Interface):
    """Configuration registry schema"""

    book_categories = schema.Dict(
        title="Catégories de livres",
        key_type=schema.ASCII(title="Identifiant"),
        value_type=schema.TextLine(title="Titre"),
        required=True,
    )
