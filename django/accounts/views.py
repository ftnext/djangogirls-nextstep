from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import (
    MyPasswordChangeForm,
)


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        """
        フォーム入力に問題がなければ、userを保存した上で読者のグループに追加。
        ログイン状態にして、success_urlに遷移させる
        """
        user = form.save()
        group = Group.objects.get(name='ReaderUser')
        user.groups.add(group)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)


class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/password_change.html'


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'
