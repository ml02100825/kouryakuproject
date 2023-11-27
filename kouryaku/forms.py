from django.forms import ModelForm
from .models import Lineups
class LineupsForm(ModelForm):
    class Meta:
        model= Lineups
        fields= ['Character', 'Map', 'title', 'comment', 'image1', 'image2', 'image3']
from .models import Comments
 
 
class CommentCreateForm(ModelForm):
    """コメントフォーム"""
    class Meta:
        model = Comments
        # exclude = ('user',  'target', 'created_at')
        fields = ['text']
 
 
