from z3c.table import column
from plone import api

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
                    state_title =  w.states[state].title or state
                    break
        except:
            pass
        return state_title
