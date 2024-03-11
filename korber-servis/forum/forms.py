from django import forms
from .models import Post, Comment, Category

class MultipleFileInput(forms.ClearableFileInput):
    template_name = 'widgets/multiple_file_input.html'  # Putanja do HTML šablona za widget


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    files = forms.FileField()
    class Meta:
        model = Post
        fields = ('content','files',)

class CommentModelForm(forms.ModelForm):
    body = forms.CharField(label='', 
                            widget=forms.TextInput(attrs={'placeholder': 'Add a comment...'}))
    files = forms.FileField()
    class Meta:
        model = Comment
        fields = ('body', 'files',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent']
