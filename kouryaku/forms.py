from django.forms import ModelForm
from django import forms
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
class ContactForm(forms.Form):
    # フォームのフィールドをクラス変数として定義
    name = forms.CharField(label ='お名前')
    email = forms.EmailField(label ='メールアドレス')
    title =  forms.CharField(label ='件名')
    message =  forms.CharField(label ='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        '''ContactFromのコンストラクター
        
            フィールドの初期化を行う
        '''
        super().__init__(*args, **kwargs)
        #nameフィールドのplaceolderにメッセージを登録
        self.fields['name'].widget.attrs['placeholder'] = \
            'お名前を入力してください'
        
        #nameフィールドを出力する<input>タグのclass属性を設定
        self.fields['name'].widget.attrs['class'] = 'form-control'

         #emailフィールドのplaceolderにメッセージを登録
        self.fields['email'].widget.attrs['placeholder'] = \
            'メールアドレスを入力してください'
        
        #emailフィールドを出力する<input>タグのclass属性を設定
        self.fields['email'].widget.attrs['class'] = 'form-control'

         #titleフィールドのplaceolderにメッセージを登録
        self.fields['title'].widget.attrs['placeholder'] = \
            'タイトルを入力してください'
        
        #titleフィールドを出力する<input>タグのclass属性を設定
        self.fields['title'].widget.attrs['class'] = 'form-control'

         #messageフィールドのplaceolderにメッセージを登録
        self.fields['message'].widget.attrs['placeholder'] = \
            'メッセージを入力してください'
        
        #messageフィールドを出力する<input>タグのclass属性を設定
        self.fields['message'].widget.attrs['class'] = 'form-control'
 
 
