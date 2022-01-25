from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from forms6.forms import UserForm
# Create your views here.
from django.views import View, generic
from forms6.models import UserModel, NewsModel, CommentModel
from forms6.forms import *


class Start(View):
    def get(self, request):
        user_form = UserForm()
        return render(request, 'forms6/register.html', {"user_form": user_form})

    def post(self, request):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            UserModel.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/page/')
        return render(request, 'forms6/register.html', {'user_form': user_form})


class NewsList(generic.ListView):
    model = NewsModel
    # context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = NewsModel.objects.order_by('create_at').reverse()
        return context


class NewsDetail(generic.DetailView):
    model = NewsModel
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_comments = []
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        for comment in CommentModel.objects.all():
            if comment.news.id == context['object'].id:
                filter_comments.append(comment)
        context['comments'] = filter_comments
        return context

    def post(self, request, pk):
        news = NewsModel.objects.filter(id=pk).first()
        new_comment = CommentForm(request.POST)
        if not new_comment.is_valid():
            new_comment = new_comment.cleaned_data
            new_comment['news'] = news
            CommentModel.objects.create(**new_comment)
            return redirect(request.path)
        return render(request, 'forms6/newsmodel_detail.html', {'comment_form': new_comment})


class Create(View):
    def get(self, request):
        news_form = NewsForm()
        return render(request, 'forms6/create_news.html', {'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            NewsModel.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/forms/')
        return render(request, 'forms6/create_news.html', {'news_form': news_form})


class Edit(View):
    def get(self, request, news_id):
        news = NewsModel.objects.get(id=news_id)
        news_form = NewsForm(instance=news)
        return render(request, 'forms6/create_news.html', {'news_form': news_form, 'news_id': news_id})

    def post(self, request, news_id):
        news = NewsModel.objects.get(id=news_id)
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            news_form = news_form.cleaned_data
            news_form['edit_at'] = datetime.date.today()
            final_form = NewsForm(news_form, instance=news)
            final_form.save()
            return HttpResponseRedirect(f'/forms/detail/{news_id}')

        return render(request, 'forms6/create_news.html', {'news_form': news_form, 'news_id': news_id})
