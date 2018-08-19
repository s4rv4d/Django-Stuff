from django import forms
from blog.models import Comment,Post

class PostForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Post
        fields = ['author','title','text']
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        return cleaned_data


class CommentForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Comment
        fields = ['author','text']
        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        return cleaned_data
