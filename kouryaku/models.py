from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from datetime import datetime, timezone
class Character(models.Model):
    title=models.CharField(
        verbose_name='キャラクター',
       max_length=20 
       )
    def __str__(self):
        return self.title

class Map(models.Model):
    title=models.CharField(
        verbose_name='マップ',
        max_length=20
    )
    def __str__(self):
        return self.title
class Lineups(models.Model):
    user= models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    Character= models.ForeignKey(
        Character,
        verbose_name='キャラクター',
        on_delete=models.PROTECT
    )
    Map= models.ForeignKey(
        Map,
        verbose_name='マップ',
        on_delete=models.PROTECT
    )
    title = models.CharField(
        verbose_name='タイトル',
        max_length=100
    )
    comment = models.TextField(
        verbose_name='説明'
    )
    image1= models.ImageField(
        verbose_name='イメージ１',
        upload_to= 'photos'
    )
    image2= models.ImageField(
        verbose_name='イメージ２',
        upload_to='photos',
        blank=True,
        null=True
        )
    image3= models.ImageField(
        verbose_name='イメージ３',
        upload_to='photos',
        blank=True,
        null=True
        )
    posted_at=models.DateField(
        verbose_name='投稿日時',
        auto_now_add=True

    )
    def __str__(self):
        return self.title

class Comments(models.Model):
    """記事に紐づくコメント"""
    user= models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    text = models.TextField('本文')
    target = models.ForeignKey(Lineups, on_delete=models.CASCADE, verbose_name='対象記事')
    posted_at=models.DateField(
        verbose_name='投稿日時',
        auto_now_add=True

    )
 
    def __str__(self):
        return self.text[:20]


    
# Create your models here.
