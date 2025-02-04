from plone import api
from plone.app.layout.viewlets import common as base

from collective.concepts.behaviors import ISpotlight


class SpotlightViewlet(base.ViewletBase):

    @property
    def infos(self):
        brains = api.content.find(
            object_provides=ISpotlight,
            is_spotlight=True,
            sort_on="created",
            sort_order="descending",
        )
        objects = [b.getObject() for b in brains[:3]]
        infos = []
        for o in objects:
            infos.append(
                {
                    "title": o.title,
                    "description": o.description,
                    "url": o.absolute_url(),
                }
            )
        return infos
