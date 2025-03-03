from plone import api
from plone.app.layout.viewlets import common as base

from collective.concepts.behaviors import IVotesMarker


class VotesViewlet(base.ViewletBase):

    def render(self):
        if not IVotesMarker.providedBy(self.context):
            return ""
        view = api.content.get_view("collective-concepts-votes-view", self.context)
        return view()

