from plone import schema
from plone.dexterity.content import Item
from plone.supermodel import model
from zope.interface import implementer


class IAuthor(model.Schema):
    """Author interface"""

    # Fields
    firstname = schema.TextLine(
        title="Prénom",
    )
    lastname = schema.TextLine(
        title="Nom",
    )
    birthday = schema.Date(
        title="Date de naissance",
        required=False,
    )


@implementer(IAuthor)
class Author(Item):
    """Author content type"""

    @property
    def title(self):
        return f"{self.firstname} {self.lastname}"

    @title.setter
    def title(self, value):
        pass
