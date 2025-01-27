from plone import api
from plone.dexterity.interfaces import IDexterityContent
from plone.restapi.interfaces import IFieldSerializer
from plone.restapi.serializer.converters import json_compatible
from zope.component import adapter
from zope.interface import implementer
from zope.schema.interfaces import IField

from collective.concepts.interfaces import IBrowserLayer


@adapter(IField, IDexterityContent, IBrowserLayer)
@implementer(IFieldSerializer)
class FieldSerializer:
    def __init__(self, field, context, request):
        self.context = context
        self.request = request
        self.field = field

    def __call__(self):
        return json_compatible(self.get_value())

    def get_value(self, default=None):
        default = getattr(self.field.interface(self.context), self.field.__name__, default)
        return "SSS - " + default if default else default
