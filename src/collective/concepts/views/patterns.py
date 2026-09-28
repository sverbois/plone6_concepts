import json

from Products.Five.browser import BrowserView


class PatternsView(BrowserView):
    @property
    def data(self):
        return [
            {"name": "Ville de Namur", "url": "https://www.namur.be", "inhabitants": 110000},
            {"name": "Ville de Liège", "url": "https://www.liege.be", "inhabitants": 200000},
            {"name": "Ville de Mons", "url": "https://www.mons.be", "inhabitants": 95000},
        ]

    @property
    def tree(self):
        return json.dumps(
            [
                {"label": "Sports", "children": [{"label": "Escalade"}, {"label": "Tennis"}]},
                {"label": "Loisirs", "children": [{"label": "Cinéma"}]},
            ]
        )
