from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorator import account_ownership_required
from accountapp.form import AccountUpdateForm
from articleapp.models import Article

# Create your views here.

has_ownership = [account_ownership_required, login_required]

class AccountCreateView(CreateView):
    model = User # User 모델을 기반으로
    form_class = UserCreationForm # 회원가입 폼 사용
    success_url = reverse_lazy('accountapp:login') # 성공하면 이동할 페이지
    template_name = 'accountapp/create.html' # 사용할 쳄플릿 파일 경로


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User # User 모델을 기반으로
    context_object_name = 'target_user'
    form_class = AccountUpdateForm# 회원가입 폼 사용
    success_url = reverse_lazy('accountapp:hello_world') # 성공하면 이동할 페이지
    template_name = 'accountapp/update.html' # 사용할 쳄플릿 파일 경로


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')  # 성공하면 이동할 페이지
    template_name = 'accountapp/delete.html'  # 사용할 쳄플릿 파일 경로

