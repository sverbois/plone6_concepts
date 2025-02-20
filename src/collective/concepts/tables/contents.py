from plone import api
from plone.dexterity.interfaces import IDexterityContent
from Products.Five import BrowserView
from z3c.table import column
from z3c.table.table import Table
from zope.interface import Interface
from zope.interface import implementer


class ContentsTableView(BrowserView):

    @property
    def table(self):
        generic_table = ContentsTable(self, self.request)
        generic_table.__parent__ = self
        generic_table.update()
        return generic_table


class IContentsTable(Interface):
    """Marker interface for collective.concepts tables"""


@implementer(IContentsTable)
class ContentsTable(Table):
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


class TitleColumn(column.LinkColumn):
    header = "Titre"
    weight = 10

    def getLinkURL(self, item):
        return item.absolute_url()

    def getLinkContent(self, item):
        return item.title

    # TODO: créer un adapteur pour la valeur du titre


class StateColumn(column.Column):
    header = "Etat"
    weight = 100

    def renderCell(self, item):
        state_title = ""
        try:
            state = api.content.get_state(obj=item)
            wtool = api.portal.get_tool("portal_workflow")
            workflows = wtool.getWorkflowsFor(item)
            if workflows:
                for w in workflows:
                    if state in w.states:
                        state_title = w.states[state].title or state
                        break
        except:
            pass
        return state_title
