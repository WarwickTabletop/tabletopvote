import random

from django.views.generic import View, TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404, HttpResponseRedirect, reverse

from .models import Election, Vote


class HomeView(ListView):
    template_name = "home.html"
    model = Election
    context_object_name = "elections"

    def get_queryset(self):
        return Election.objects.filter(active=True)


class DoneView(DetailView):
    model = Vote
    slug_field = "uuid"
    template_name = "done.html"

    def get_queryset(self):
        self.election = get_object_or_404(Election, id=self.kwargs['election'])
        return self.election.vote_set.all()


# Create your views here.
class VoteView(TemplateView):
    template_name = "votescreen.html"

    def post(self, request, **kwargs):
        self.get_context_data(**kwargs)
        print(request.POST)
        errors = []
        if "selection" not in request.POST:
            errors.append("Please select at least one option")
            selection = []
        else:
            selection = request.POST.getlist("selection")
        if 0 < self.election.max_votes < len(selection):
            errors.append("Too many options selected")
        try:
            selection = [int(s) for s in selection]
        except ValueError:
            errors.append("Invalid option submitted")
        for i in selection:
            allowed = [a.id for a in self.election.option_set.all()]
            if i not in allowed:
                errors.append("Unknown option selected")

        if errors:
            return self.get(request, errors=errors)
        else:
            vote = Vote(
                ip=request.META['REMOTE_ADDR'],
                election=self.election,
            )
            vote.save()
            vote.selections.add(*selection)
            return HttpResponseRedirect(reverse("vote:vote_done", kwargs={'election':self.election.id, 'slug':vote.uuid}))

    def get_context_data(self, **kwargs):
        ctxt = super().get_context_data(**kwargs)
        self.election = get_object_or_404(Election, id=self.kwargs['id'], active=True)
        ctxt['election'] = self.election
        ctxt['choices'] = list(self.election.option_set.all())
        random.shuffle(ctxt['choices'])
        return ctxt
