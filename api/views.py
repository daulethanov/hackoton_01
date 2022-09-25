from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.db.models import F

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView

from .forms import *


class Home(ListView):
    model = User
    template_name = 'base.html'
    context_object_name = 'user'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('account')


def logout_user(request):
    logout(request)
    return redirect('home')


def model_form_upload(request):
    if request.method == 'POST':
        form = CheckDocument(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CheckDocument()
    return render(request, 'UserDetail.html', {
        'detail': Document.objects.all(),
        'form': form,
    })


def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'index.html', {'form': form})


def account_view(request):
    if request.user.groups.filter(name='manager').exists():
        return model_form_upload(request)
    else:
        return upload_file(request)
    return render(request)