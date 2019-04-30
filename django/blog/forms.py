from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """Bootstrap4のform-controlクラスを追加する
        （ラジオボタンやセレクトボックスがないため副作用はなし）
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = ('title', 'text',)
