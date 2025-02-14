from plone import api
from plone.dexterity.interfaces import IDexterityContent
from Products.Five import BrowserView
from z3c.table import column
from z3c.table.table import Table
from zope.component import adapter
from zope.interface import implementer

from .interfaces import IContentsTable


class GenericView(BrowserView):

    def table(self):
        generic_table = ContentTable(self, self.request)
        generic_table.__parent__ = self
        generic_table.update()
        return generic_table


@implementer(IContentsTable)
class ContentTable(Table):
    cssClasses = {
        "table": "table table-bordered",
    }


class ContentsTableValues(object):

    def __init__(self, context, request, table):
        self.context = context
        self.request = request
        self.table = table

    @property
    def values(self):
        values = [item.getObject() for item in api.content.find(object_provides=IDexterityContent)]
        return values
