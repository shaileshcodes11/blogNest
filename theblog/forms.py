from django import forms
from .models import Post,Category,Comment
from django_ckeditor_5.widgets import CKEditor5Widget

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditor5Widget(config_name='default'), required=False)

    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippet', 'header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            
        }


class EditForm(forms.ModelForm):        
    # body = forms.CharField(widget=CKEditorWidget(), required=False)
    body = forms.CharField(widget=CKEditor5Widget(config_name="default"), required=False)


    class Meta:
        model = Post
        fields = ('title','title_tag','category','body','snippet','header_image')
        # fields = ('title', 'title_tag', 'category', 'body','snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            # 'body': forms.Textarea(attrs={'class':'form-control'}),                        
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),


    }
        


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }
        