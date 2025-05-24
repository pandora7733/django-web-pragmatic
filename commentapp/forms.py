from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreattionForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
