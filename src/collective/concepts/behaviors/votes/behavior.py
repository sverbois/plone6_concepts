from persistent.dict import PersistentDict
from persistent.list import PersistentList
from plone import api
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from zope import schema
from zope.annotation.interfaces import IAnnotations
from zope.interface import Attribute
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IVotesMarker(Interface):
    """Marker of content for which we can vote."""


# @provider(IFormFieldProvider)
# class IVotesBehavior(model.Schema):
# fieldset(
#     "debug",
#     label="Debug",
#     fields=("votes", "voted"),
# )

# votes = schema.Dict(
#     title="Vote infos",
#     key_type=schema.Int(title="Vote value"),
#     value_type=schema.TextLine(title="User id"),
#     required=False,
# )
# if not api.env.debug_mode(): directives.omitted("votes")
# fieldset("debug", label="Debug", fields=("votes"),


class IVotesBehavior(Interface):
    votes = Attribute("Votes")  # {"sverbois": 4, "cadams":4, "admin":5}
    mean = Attribute("Votes mean")

    def vote(userid, vote):
        """Store the vote of userid"""

    def remove_vote(userid):
        """Remove the vote of userid"""

    def has_votes():
        """Return whether anybody ever voted for this item"""

    def has_already_voted(userid):
        """Return the information wether a person already voted."""

    def clear():
        """Clear all the votes."""


KEY = "collective.concepts.behavior.votes"


@implementer(IVotesBehavior)
class VotesAdapter(object):
    def __init__(self, context):
        self.context = context
        annotations = IAnnotations(context)
        if KEY not in annotations.keys():
            annotations[KEY] = PersistentDict({})
        self.votes = annotations[KEY]

    @property
    def mean(self):
        if not self.votes:
            return 0
        return sum(self.votes.values()) / len(self.votes)

    def vote(self, userid, vote):
        if vote not in range(1, 6):
            raise ValueError("Vote must be between 1 and 5")
        if self.has_already_voted(userid):
            raise KeyError("You may not vote twice")
        self.votes[userid] = vote

    def remove_vote(self, userid):
        if userid in self.votes:
            del self.votes[userid]

    def has_votes(self):
        return len(self.votes) != 0

    def has_already_voted(self, userid):
        return userid in self.votes

    def clear(self):
        annotations = IAnnotations(self.context)
        annotations[KEY] = PersistentDict({})
        self.votes = annotations[KEY]
