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
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views.generic import FormView


class IndexView(ListView):
    template_name = "index.html"
    model = Lineups
    queryset = Lineups.objects.order_by('-posted_at')
    paginate_by= 9

class MapView(ListView):
    template_name = "index.html"
    model = Lineups

    paginate_by= 9
    def get_queryset(self):
        category_id=self.kwargs['Map']
        categories= Lineups.objects.filter(
            Map=category_id).order_by('posted_at')
        return categories

class CharacterView(ListView):
    template_name = "index.html"
    model = Lineups

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


    def get_context_data(self, **kwargs):
        post_pk = self.kwargs['pk']
        detail = get_object_or_404(Lineups, pk=post_pk)
        context = super().get_context_data(**kwargs)
        context.update({"detail":detail,
                        "comments":Comments.objects.filter(target=detail.id)
        })
        return context
class ContactView(FormView):
    # '''問い合わせページを表示するビュー
    
    # フォームで入力されたデータを取得し、メールの作成と返信を行う
    # '''
    #contct.htmlをレンダリングする
        template_name ='contact.html'
    
        #クラス変換form_classにform.pyで定義したContactFromを設定
        form_class = ContactForm
        #送信完了後にリダイレクトするページ
        success_url = reverse_lazy('kouryaku:index')

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            print(context['form'])
            return context

        def form_valid(self, form):
    

            name =  form.cleaned_data['name']
            email =  form.cleaned_data['email']
            title =  form.cleaned_data['title']
            message =  form.cleaned_data['message']
        #     #メールのタイトルの書式を設定   
            subject =  'お問い合わせ: {}'.format(title)

        #     #フォームの入力データの書式を設定
            message = \
            '送信者名: {0}\nメールアドレス: {1}\n タイトル: {2}\n メッセージ:\n{3}' \
           .format(name, email, title , message)

            from_email = 'admin@example.com'

            to_list = ['halu.825.bakura@gmail.com']

        #     # Email Messageオブジェクトを生成
            message = EmailMessage(subject=subject, 
                                body=message,
                                from_email=from_email,
                                to=to_list,          
            )
        #     #EmailMessage   クラスのsend()でメールサーバからメールを送信
            message.send()
        #     #送信後に完了するメッセージ
            messages.success(
                self.request, 'お問い合わせは正常に送信されました。')
        #     # 戻り値はスーパークラスの form_valid()の戻り値(HttpResponseRedirect)
            return super().form_valid(form)

   
    
 
  





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


    
    def form_valid(self, form):

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
class CommentEditView(UpdateView):
        template_name = 'comment_edit.html'
        model = Comments
        
        fields = ['text']

        
        success_url = reverse_lazy('kouryaku:post_detail', )
    
        def form_valid(self, form):
                
                postdata = form.save(commit=False)
                postdata.posted_at = datetime.now()
                postdata.save()
                return super().form_valid(form)
        



