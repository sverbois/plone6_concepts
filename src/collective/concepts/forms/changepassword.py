from plone import api
from plone import schema
from plone.autoform.form import AutoExtensibleForm
from plone.supermodel import model
from z3c.form import button
from z3c.form import form
from zope.interface import Invalid
from zope.interface import invariant


def validate_new_password(value):
    if len(value) < 8:
        raise Invalid("Votre mot de passe doit contenir au moins 8 caractères.")
    return True


class IChangePassword(model.Schema):

    eid = schema.TextLine(
        title="Identifiant",
        description="Entrez votre eid.",
    )
    current_password = schema.Password(
        title="Mot de passe actuel",
        description="Entrez votre mot de passe actuel.",
    )
    new_password = schema.Password(
        title="Nouveau mot de passe",
        description="Entrez votre nouveau mot de passe. 8 caractères minimum.",
        constraint=validate_new_password,
    )
    confirmed_password = schema.Password(
        title="Confirmer le nouveau mot de passe",
        description="Entrez à nouveau le mot de passe pour confirmation.",
    )

    @invariant
    def validate_data(data):
        if data.new_password != data.confirmed_password:
            raise Invalid("La confirmation de votre nouveau mot de passe est incorrecte.")


class ChangePassword(AutoExtensibleForm, form.Form):

    schema = IChangePassword
    ignoreContext = True

    label = "Changer de mot de passe"
    description = "Utiliser ce formulaire pour changer votre mot de passe."

    @button.buttonAndHandler("Changer le mot de passe")
    def handleChange(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        # DO SOMETHING WITH THE DATA
        print(data)
        api.portal.show_message(message="Votre mot de passe a été changé.", request=self.request, type="info")
        self.request.response.redirect(self.context.absolute_url())
