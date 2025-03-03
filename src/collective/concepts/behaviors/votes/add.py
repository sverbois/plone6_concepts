from plone import api
from plone import schema
from plone.app.z3cform.widgets.radio import RadioFieldWidget
from plone.autoform import directives
from plone.autoform.form import AutoExtensibleForm
from z3c.form import button
from z3c.form import form
from zope.interface import Interface

from collective.concepts.behaviors import IVotesBehavior


class IVotesForm(Interface):
    """Schema Interface for IMyForm
    Define your form fields here.
    """

    vote = schema.Choice(
        title="Votre vote",
        values=[1, 2, 3, 4, 5],
    )
    directives.widget("vote", RadioFieldWidget, klass="sebastien")


class VotesForm(AutoExtensibleForm, form.Form):
    schema = IVotesForm
    ignoreContext = True

    label = "Voter"
    description = "Indiquer votre avis sur ce livre."

    @button.buttonAndHandler("Voter")
    def handleApply(self, action):

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        current_user_id = api.user.get_current().getId()
        behavior = IVotesBehavior(self.context)
        behavior.vote(current_user_id, data["vote"])
        api.portal.show_message("Votre vote a été pris en compte.", self.request, type="info")

    # @button.buttonAndHandler("Annuler")
    # def handleCancel(self, action):
    #     """User cancelled. Redirect back to the front page.
    #     """
