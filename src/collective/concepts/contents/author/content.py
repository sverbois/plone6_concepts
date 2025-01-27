from plone import schema
from plone.app.textfield import RichText
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from z3c.form.browser.radio import RadioFieldWidget
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
