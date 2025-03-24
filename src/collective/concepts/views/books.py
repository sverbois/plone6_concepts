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
                    "fullname": a.firstname + " " + a.lastname,
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

    @property
    def authors(self):
        brains = api.content.find(portal_type="Author", sort_on="sortable_title")
        authors = [b.getObject() for b in brains]
        infos = []
        for a in authors:
            books = [
                r.from_object
                for r in api.relation.get(target=a, relationship="authors")
                if r.from_object.portal_type == "Book"
            ]
            books_infos = [
                {
                    "title": b.title,
                    "url": b.absolute_url(),
                }
                for b in books
            ]
            infos.append(
                {
                    "title": a.title,
                    "url": a.absolute_url(),
                    "books": books_infos,
                }
            )
        return infos
