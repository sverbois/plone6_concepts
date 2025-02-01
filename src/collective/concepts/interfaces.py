from plone import schema
from zope.interface import Interface


class IBrowserLayer(Interface):
    """Browser layer marker interface"""


class ISettings(Interface):
    """Configuration registry schema"""

    book_publishers = schema.Dict(
        title="Book publishers",
        key_type=schema.TextLine(title="Publisher id"),
        value_type=schema.TextLine(title="Publisher name"),
        required=True,
    )
    shop_url = schema.URI(
        title="Shop URL",
        required=False,
    )
