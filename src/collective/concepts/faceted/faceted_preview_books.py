from collective.concepts.vocabularies import get_title_from_vocabulary_value
from eea.facetednavigation.utils import truncate
from plone import api
from Products.Five.browser import BrowserView


class FacetedPreviewBooks(BrowserView):
    """Helper for the "Books preview" faceted view."""

    def tiles(self, brains):
        images = api.portal.get_navigation_root(self.context).restrictedTraverse("@@image_scale")
        tiles = []
        for brain in brains:
            category = get_title_from_vocabulary_value("collective.taxonomy.bookcategories", brain.book_category)
            cover = images.tag(brain, "cover", scale="mini", css_class="card-img-top") or ""
            tiles.append(
                {
                    "title": brain.Title,
                    "url": brain.getURL(),
                    "description": truncate(brain.Description),
                    "cover": cover,
                    "category": category,
                }
            )
        return tiles
