import requests
from Products.Five.browser import BrowserView


class InfradocView(BrowserView):

    @property
    def applications(self):
        response = requests.get("https://infradoc.imio.be/applications")
        apps = response.json()["applications"]
        items = []
        for a in apps:
            infos = {
                "name": a["application_name"],
                "url": a["vhost_name"],
                "size": a["total_size"],
            }
            items.append(infos)
        return sorted(items, key=lambda item: item["name"])
