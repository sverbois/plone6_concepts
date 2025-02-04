from plone import api
from plone.app.layout.viewlets import common as base

from collective.concepts.behaviors import IPriceBehavior


class PriceViewlet(base.ViewletBase):

    @property
    def price_net(self):
        return "{:.2f}".format(IPriceBehavior(self.context).price_net)

    @property
    def price_vat(self):
        return "{:.2f}".format(IPriceBehavior(self.context).price_vat)

    @property
    def price_gross(self):
        return "{:.2f}".format(IPriceBehavior(self.context).price_gross)
