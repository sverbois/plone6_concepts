from plone import api
from plone.app.layout.viewlets import common as base


class InfosViewlet(base.ViewletBase):

    @property
    def message(self):
        return "Hello World !!!"

    @property
    def count(self):
        brains = api.content.find(portal_type="Document")
        return len(brains)
