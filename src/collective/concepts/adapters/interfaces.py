from zope.interface import Attribute
from zope.interface import Interface


class IRichTitle(Interface):
    """Marker interface for richt title"""

    rich_title = Attribute("Rich title")
