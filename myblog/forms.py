from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

        CHOICES=[('select1','select 1'),
         ('select2','select 2')]

        like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())        
