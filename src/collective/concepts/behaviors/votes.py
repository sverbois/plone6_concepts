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


@provider(IFormFieldProvider)
class IVotesBehavior(model.Schema):
    # if not api.env.debug_mode():
    directives.omitted("votes")
    directives.omitted("voted")

    fieldset(
        "debug",
        label="Debug",
        fields=("votes", "voted"),
    )

    votes = schema.Dict(
        title="Vote info",
        key_type=schema.TextLine(title="Vote category"),
        value_type=schema.Int(title="Vote number"),
        required=False,
    )
    voted = schema.List(
        title="User who voted",
        value_type=schema.TextLine(),
        required=False,
    )

    mean = Attribute("Votes mean")

    def vote(userid, vote):
        """Store the vote information"""

    def has_votes():
        """Return whether anybody ever voted for this item"""

    def has_already_voted(userid):
        """Return the information wether a person already voted."""

    def clear():
        """Clear the votes."""


KEY = "collective.concepts.behavior.vote"


@implementer(IVotesBehavior)
class VotesAdapter(object):
    def __init__(self, context):
        self.context = context
        annotations = IAnnotations(context)
        if KEY not in annotations.keys():
            annotations[KEY] = PersistentDict({"voted": PersistentList(), "votes": PersistentDict()})
        self.annotations = annotations[KEY]

    @property
    def votes(self):
        return self.annotations["votes"]

    @property
    def voted(self):
        return self.annotations["voted"]

    @property
    def mean(self):
        votes = self.annotations["votes"]
        if not votes:
            return 0
        total = count = 0
        for vote, number in votes.items():
            total += vote * number
            count += number
        return total / count

    def vote(self, userid, vote):
        if vote not in range(1, 6):
            raise ValueError("Vote must be between 1 and 5")
        # if self.has_already_voted(userid):
        #     raise KeyError("You may not vote twice")
        self.annotations["voted"].append(userid)
        votes = self.annotations["votes"]
        if vote not in votes:
            votes[vote] = 1
        else:
            votes[vote] += 1

    def has_votes(self):
        return len(self.annotations.get("votes", [])) != 0

    def has_already_voted(self, userid):
        return userid in self.annotations["voted"]

    def clear(self):
        annotations = IAnnotations(self.context)
        annotations[KEY] = PersistentDict({"voted": PersistentList(), "votes": PersistentDict()})
        self.annotations = annotations[KEY]
