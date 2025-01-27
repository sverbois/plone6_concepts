from setuptools import find_packages
from setuptools import setup

setup(
    name="collective.concepts",
    packages=find_packages("src"),
    namespace_packages=["collective"],
    package_dir={"": "src"},
    install_requires=[
        "collective.taxonomy",
        "eea.facetednavigation",
        "Products.CMFPlone",
        "requests",
        "z3c.jbot",
        "z3c.table",
    ],
    entry_points="""
        [plone.autoinclude.plugin]
        target = plone
    """,
)
