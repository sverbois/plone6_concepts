from plone import api
from Products.Five import BrowserView
from z3c.table import column
from z3c.table.table import Table
from .interfaces import IGenericTable
from zope.interface import implementer
from zope.component import adapter
from plone.dexterity.interfaces import IDexterityContent

class GenericView(BrowserView):

    def table(self):
        generic_table = ContentTable(self, self.request)
        generic_table.__parent__ = self
        generic_table.update()
        return generic_table

@implementer(IGenericTable)
class ContentTable(Table):
    cssClasses = {
        "table": "table table-bordered",
    }
    # @property
    # def values(self):
    #     values = [item.getObject() for item in api.content.find(object_provides=IDexterityContent)]
    #     return values


class GenericTableValues(object):

    def __init__(self, context, request, table):
        self.context = context
        self.request = request
        self.table = table

    @property
    def values(self):
        values = [item.getObject() for item in api.content.find(object_provides=IDexterityContent)]
        return values