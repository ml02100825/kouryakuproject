from django.urls import path
from . import views


app_name = 'kouryaku'

urlpatterns=[
    path("", views.IndexView.as_view(),     name="index"),
    path('post/', views.CreateLineupView.as_view(), name='post'),
    path("post_done/", views.PostSuccessView.as_view(), name='post_done'),
    path("posts/Character/<int:Map>", views.MapView.as_view(), name='post_map'),
    path("posts/<int:Character>", views.CharacterView.as_view(), name='post_character'),
    path("user-list/<int:user>", views.UserView.as_view(), name='user_list'),
    path('post_detail/<int:pk>', views.DetailView.as_view(), name='post_detail'),
    path("mypage/", views.MypageView.as_view(), name='mypage'),
    path("post_detail/<int:pk>/delete/", views.PostDeleteView.as_view(), name='post_delete'),
    path('post_detail/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('post_detail/<int:pk>/comment/create/', views.CommentCreate.as_view(), name='comment_create'), 
    path('post_detail/<int:pk>/comment/edit/', views.CommentEditView.as_view(), name='comment_edit'),
    path("contact/", views.ContactView.as_view(), name='contact'
    ),
    path('post_edit_success', views.PostEditSuccessView.as_view(), name='post_edit_success')


    
    ]