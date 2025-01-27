from plone import api
from Products.Five import BrowserView
from z3c.table import column
from z3c.table.table import Table


class BooksView(BrowserView):

    def table(self):
        books_table = BooksTable(self, self.request)
        books_table.__parent__ = self
        books_table.update()
        return books_table


class BooksTable(Table):
    cssClasses = {
        "table": "table table-bordered",
    }

    # sortOrder = "ascending"
    # sortOn = "table-isbn-1"

    startBatchingAt = 999999
    batchSize = 999999

    @property
    def values(self):
        criteria = {"portal_type": "Book"}
        values = [item.getObject() for item in api.content.find(**criteria)]
        return values

    def setUpColumns(self):
        return [
            column.addColumn(self, TitleColumn, name="title"),
            column.addColumn(self, column.GetAttrColumn, name="isbn", attrName="isbn", header="ISBN", weight=40),
            column.addColumn(self, StateColumn, name="status"),
        ]


class TitleColumn(column.LinkColumn):
    header = "Titre"
    weight = 10

    def getLinkURL(self, item):
        return item.absolute_url()

    def getLinkContent(self, item):
        return item.title


class StateColumn(column.Column):
    header = "Etat"
    weight = 100

    def renderCell(self, item):
        state = api.content.get_state(obj=item)
        wtool = api.portal.get_tool("portal_workflow")
        workflows = wtool.getWorkflowsFor(item)
        if workflows:
            for w in workflows:
                if state in w.states:
                    return w.states[state].title or state
        return state
