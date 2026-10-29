from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label='Seu nome')
    email = forms.EmailField(label='Seu e-mail')
    to = forms.EmailField(label='Enviar para')
    comments = forms.CharField(required=False, widget=forms.Textarea, label='Comentários (opcional)')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']