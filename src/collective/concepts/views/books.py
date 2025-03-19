from plone import api
from Products.Five.browser import BrowserView


class BooksView(BrowserView):

    @property
    def books(self):
        brains = api.content.find(portal_type="Book", sort_on="sortable_title")
        books = [b.getObject() for b in brains]
        infos = []
        for b in books:
            authors = [r.to_object for r in api.relation.get(source=b, relationship="authors")]
            authors_infos = [
                {
                    "fullname": a.title,
                    "url": a.absolute_url(),
                }
                for a in authors
            ]
            infos.append(
                {
                    "title": b.title,
                    "description": b.description,
                    "url": b.absolute_url(),
                    "authors": authors_infos,
                }
            )
        return infos
