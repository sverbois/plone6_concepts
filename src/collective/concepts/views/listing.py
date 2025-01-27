from plone import api
from Products.Five.browser import BrowserView


class ListingView(BrowserView):

    @property
    def pages(self):
        catalog = api.portal.get_tool("portal_catalog")
        brains = catalog.searchResults(portal_type="Document", sort_on="created", sort_order="ascending")
        infos = [
            {
                "title": b.Title,
                "description": b.Description,
                "url": b.getURL(),
            }
            for b in brains
        ]
        # objects = [b.getObject() for b in brains]
        # infos = [
        #     {
        #         "title": o.title,
        #         "description": o.description,
        #         "url": o.absolute_url(),
        #     }
        #     for o in objects
        # ]
        return infos
