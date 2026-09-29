from plone import api
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.concepts.behaviors import IVotesBehavior


class BaseView(BrowserView):
    index = ViewPageTemplateFile("view.pt")

    @property
    def behavior(self):
        return IVotesBehavior(self.context)

    @property
    def current_user_id(self):
        return api.user.get_current().getId()

    @property
    def can_vote(self):
        is_authenticated = not api.user.is_anonymous()
        has_already_voted = self.behavior.has_already_voted(self.current_user_id)
        return is_authenticated and not has_already_voted

    @property
    def has_vote(self):
        is_authenticated = not api.user.is_anonymous()
        has_already_voted = self.behavior.has_already_voted(self.current_user_id)
        return is_authenticated and has_already_voted

    @property
    def can_clear_votes(self):
        return api.user.has_permission("Manage portal", username=self.current_user_id)

    @property
    def vote_number(self):
        return len(self.behavior.votes)

    @property
    def mean_on_ten(self):
        return round(self.behavior.mean * 2)

    def handle_request(self):
        raise NotImplementedError

    def __call__(self):
        self.handle_request()
        return self.index()


class ViewView(BaseView):
    def handle_request(self):
        pass


class RemoveView(BaseView):
    def handle_request(self):
        if self.behavior.has_already_voted(self.current_user_id):
            self.behavior.remove_vote(self.current_user_id)


class ClearView(BaseView):
    def handle_request(self):
        if self.can_clear_votes:
            self.behavior.clear()
