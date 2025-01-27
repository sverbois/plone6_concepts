from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class NonInstallable(object):
    def getNonInstallableProfiles(self):
        """Hide unwanted profiles."""
        return [
            "collective.concepts:uninstall",
        ]

    def getNonInstallableProducts(self):
        """Hide unwanted products."""
        return [
            "collective.concepts.upgrades",
        ]
