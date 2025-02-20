import transaction
from plone import api
from plone.app.layout.viewlets import common as base
from Products.Five.browser import BrowserView

from collective.concepts.behaviors import IVotesBehavior
from collective.concepts.behaviors import IVotesMarker


class VotesView(BrowserView):
    @property
    def api(self):
        return IVotesBehavior(self.context)

    @property
    def current_user_id(self):
        return api.user.get_current().getId()

    @property
    def can_vote(self):
        is_authenticated = not api.user.is_anonymous()
        has_already_voted = self.api.has_already_voted(self.current_user_id)
        return is_authenticated and not has_already_voted

    @property
    def can_clear_votes(self):
        return api.user.has_permission("Manage portal", username=self.current_user_id)

    @property
    def vote_number(self):
        return len(self.api.voted)

    @property
    def mean_on_ten(self):
        return int(self.api.mean * 2)

    def handle_post(self):
        if "give_vote" in self.request.form and self.can_vote:
            vote = self.request.form.get("vote")
            if not vote or not vote.isdigit():
                return
            vote = int(vote)
            self.api.vote(self.current_user_id, vote)
        elif "clear_votes" in self.request.form and self.can_clear_votes:
            self.api.clear()

    def __call__(self):
        if self.request.method == "POST":
            self.handle_post()
        return self.index()


class VotesViewlet(base.ViewletBase):

    def render(self):
        if not IVotesMarker.providedBy(self.context):
            return ""
        view = api.content.get_view("collective.concepts.votes", self.context)
        return view()
