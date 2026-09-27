from decimal import Decimal

from plone.autoform.interfaces import IFormFieldProvider
from plone.indexer import indexer
from plone.supermodel import directives
from plone.supermodel import model
from zope import schema
from zope.interface import Attribute
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IPriceMarker(Interface):
    """Marker for content that has a price."""


@provider(IFormFieldProvider)
class IPriceBehavior(model.Schema):

    price_net = schema.Decimal(
        title="Price (net)",
        required=True,
    )
    price_vat = Attribute("VAT 20% of net price")
    price_gross = Attribute("Price gross (net + VAT 20%")


@implementer(IPriceBehavior)
class PriceAdapter:
    def __init__(self, context):
        self.context = context

    @property
    def price_net(self):
        """Getter, read from context and return back"""
        return self.context.price_net

    @price_net.setter
    def price_net(self, value):
        """Setter, called by the form, set on context"""
        self.context.price_net = value

    @property
    def price_vat(self):
        return self.price_net * Decimal(0.21)

    @property
    def price_gross(self):
        return self.price_net + self.price_vat
