from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import LineupsForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Lineups
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from datetime import datetime, timezone
from .models import Comments
from .forms import CommentCreateForm
from django.shortcuts import redirect, get_object_or_404
from base.views import BaseView


class IndexView(ListView):
    template_name = "index.html"
    queryset = Lineups.objects.order_by('-posted_at')
    paginate_by= 9

class MapView(ListView):
    template_name = "index.html"

    paginate_by= 9
    def get_queryset(self):
        category_id=self.kwargs['Map']
        categories= Lineups.objects.filter(
            Map=category_id).order_by('posted_at')
        return categories

class CharacterView(ListView):
    template_name = "index.html"

    paginate_by= 9
    def get_queryset(self):
        category_id=self.kwargs['Character']
        categories= Lineups.objects.filter(
            Character=category_id).order_by('posted_at')
        return categories


class MapView(ListView):
    template_name = "index.html"

    paginate_by= 9
    def get_queryset(self):
        category_id=self.kwargs['Map']
        categories= Lineups.objects.filter(
            Map=category_id).order_by('posted_at')
        return categories

class UserView(ListView):
    template_name = "index.html"

    paginate_by= 9
    def get_queryset(self):
        user_id=self.kwargs['user']
        user_list= Lineups.objects.filter(
            user=user_id).order_by('posted_at')
        return user_list

class DetailView(DetailView):
    template_name= "detail.html"
    model = Lineups
    # queryset = Comments.objects.all().select_related()
    # queryset = Comments.objects.all().prefetch_related("lineup_set")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'comments' : Comments.objects.filter(target_id=Comments.objects.all().prefetch_related("target_id"))
            # 'comments' : Comments.objects.filter(target_id=Lineups.comment)
            # 'comments': Lineups.objects.filter(comments=self.kwargs['comments']),
        })
        return context
        
    # def post(self, request, *args, **kwargs):

    #     form = CommentCreateForm(self.request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return CommentCreateForm('/post_detail/' %id, '/create_comment')
    
        # template_name = 'comment_form.html'
        # model = Comments
        # form_class = CommentCreateForm
        # print(request)
        # return Lineups.objects.filter(id = request.POST[id])





@method_decorator(login_required, name='dispatch')

class CreateLineupView(CreateView):
    form_class = LineupsForm
    template_name = "post_lineup.html"
    success_url = reverse_lazy('kouryaku:post_done')
    def form_valid(self, form):
        postdata= form.save(commit=False)
        postdata.user=self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = 'post_success.html'

class MypageView(ListView):
    template_name='mypage.html'
    paginate_by =9
    def get_queryset(self):
        queryset = Lineups.objects.filter(
            user=self.request.user).order_by('posted_at')
        return queryset

class PostDeleteView(DeleteView):
    model = Lineups
    template_name = 'post_delete.html'
    success_url = reverse_lazy('kouryaku:mypage')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class PostEditView(UpdateView):
    template_name = 'post_edit.html'
    model = Lineups
      
    fields = ('Character', 'Map', 'title', 'comment','image1', 'image2','image3')
    success_url = reverse_lazy('kouryaku:mypage')
 
    def form_valid(self, form):
            postdata = form.save(commit=False)
            postdata.posted_at = datetime.now()
            postdata.save()
            return super().form_valid(form)

class CommentCreate(CreateView):
    """コメント投稿ページのビュー"""
    template_name = 'comment_form.html'
    model = Comments
    form_class = CommentCreateForm

    # def get(self, request, *args, **kwargs,):
    #     print(request.GET.get('detail_id'))
    #     context = super().get_context_data(**kwargs)
    #     return context
    
    def form_valid(self, form):
        # postdata= form.save(commit=False)
        # postdata.user=self.request.user
        # postdata.save()
        # return super().form_valid(form)
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Lineups, pk=post_pk)
        comment = form.save(commit=False)
        comment.user=self.request.user
        comment.target = post
        comment.save()
        return redirect('kouryaku:post_detail', pk=post_pk)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kouryaku'] = get_object_or_404(Lineups, pk=self.kwargs['pk'])
        return context


# Create your views here.
