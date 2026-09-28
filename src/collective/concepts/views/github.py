import requests
from Products.Five.browser import BrowserView


class GithubView(BrowserView):
    @property
    def repositories(self):
        response = requests.get(
            "https://api.github.com/orgs/plone/repos",
            params={"per_page": 100},
        )
        repos = response.json()
        items = []
        for repo in repos:
            infos = {
                "name": repo["name"],
                "url": repo["html_url"],
                "size": repo["size"],
            }
            items.append(infos)
        return sorted(items, key=lambda item: item["name"])
