from django.shortcuts import render
from page.models import *
from django.views import View, generic


class AdvListView(generic.ListView):
    model = Adv
    context_object_name = 'ads'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class AdvDetailView(generic.DetailView):
    model = Adv
    context_object_name = 'ob'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        views_change = context['object']
        views_change.views += 1
        views_change.save()
        return context
