from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


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
