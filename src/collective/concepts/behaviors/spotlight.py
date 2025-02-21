from plone.autoform.interfaces import IFormFieldProvider
from plone.indexer import indexer
from plone.supermodel import directives
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class ISpotlight(model.Schema):

    is_spotlight = schema.Bool(
        title="This content is in the spotlight",
        required=False,
    )

    directives.fieldset(
        "categorization",
        label="Categorization",
        fields=("is_spotlight",),
    )
