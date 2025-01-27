import json

from Products.Five.browser import BrowserView


class PatternsView(BrowserView):
    @property
    def data(self):
        return []

    @property
    def tree(self):
        return json.dumps(
            [
                {"label": "Sports", "children": [{"label": "Escalade"}, {"label": "Tennis"}]},
                {"label": "Loisirs", "children": [{"label": "Cinéma"}]},
            ]
        )
