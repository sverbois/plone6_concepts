from plone import api
from plone.dexterity.interfaces import IDexterityContent
from zope.component import adapter
from zope.interface import implementer

from collective.concepts.contents import IBook

from .interfaces import IRichTitle


@adapter(IDexterityContent)
@implementer(IRichTitle)
class RichTitleAdapterForDexterityContent(object):

    def __init__(self, content):
        self.content = content

    @property
    def rich_title(self):
        content_portal_type = self.content.portal_type
        portal_types_tool = api.portal.get_tool("portal_types")
        type_info = portal_types_tool.get(content_portal_type)
        type_title = type_info.Title() if type_info else "Unknown"
        return f"{type_title} - {self.content.title}"


@adapter(IDexterityContent)
@implementer(IRichTitle)
class DateRichTitleAdapterForDexterityContent(object):

    def __init__(self, content):
        self.content = content

    @property
    def rich_title(self):
        return f"{self.content.created().strftime('%d/%m/%Y')} - {self.content.title}"


@adapter(IBook)
@implementer(IRichTitle)
class RichTitleAdapterForBook(RichTitleAdapterForDexterityContent):

    def __init__(self, content):
        self.content = content

    @property
    def rich_title(self):
        super_title = super().get_rich_title()
        return f"{super_title} (ISBN-{self.content.isbn13})"
