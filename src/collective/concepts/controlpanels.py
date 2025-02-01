from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout

from .interfaces import ISettings


class SettingsControlPanelForm(RegistryEditForm):
    schema = ISettings
    schema_prefix = "collective.concepts"
    label = "Collective Concepts Settings"


SettingsControlPanelView = layout.wrap_form(SettingsControlPanelForm, ControlPanelFormWrapper)
