from plone import api
from plone import schema
from plone.autoform.form import AutoExtensibleForm
from plone.supermodel import model
from z3c.form import button
from z3c.form import form


class IAskQuestion(model.Schema):

    category = schema.Choice(
        title="Catégorie du message",
        values=["", "Question", "Suggestion", "Autre"],
    )
    subject = schema.TextLine(
        title="Sujet du message",
    )
    body = schema.Text(
        title="Contenu du message",
    )


class AskQuestion(AutoExtensibleForm, form.Form):

    schema = IAskQuestion
    ignoreContext = True

    label = "Contacter le support"
    description = "Utiliser ce formulaire si vous avez une question."

    @button.buttonAndHandler("Envoyer le message")
    def handleChange(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        # DO SOMETHING WITH THE DATA
        print(data)
        api.portal.show_message(message="Votre message a été envoyé.", request=self.request, type="info")
        self.request.response.redirect(self.context.absolute_url())
