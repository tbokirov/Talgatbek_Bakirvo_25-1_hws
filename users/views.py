from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from users.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.views.generic import ListView, RedirectView, CreateView


# Create your views here.

# def login_view(request):
#     if request.method == 'GET':
#         context = {
#             'form': LoginForm
#         }
#         return render(request, 'users/login.html', context=context)
#
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data.get('username'),
#                 password=form.cleaned_data.get('password')
#             )
#             if user:
#                 login(request, user)
#                 return redirect('/products')
#             else:
#                 form.add_error('username', 'Неправильный логин или пароль')
#
#     return render(request, 'users/login.html', context={
#         'form': form
#     })

class LoginView(ListView, CreateView):
    template_name = 'users/login.html'

    def get(self, request, **kwargs):
        context = {
            'form': LoginForm
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/products')
            else:
                form.add_error('username', 'Неправильный логин или пароль')

        return render(request, 'users/login.html', context={
            'form': form
        })


# def logout_view(request):
#     logout(request)
#     return redirect('/products/')


class LogoutView(RedirectView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/products/')


# def register_view(request):
#     if request.method == 'GET':
#         context = {
#             'form': RegisterForm
#         }
#         return render(request, 'users/register.html', context=context)
#
#     if request.method == 'POST':
#         form = RegisterForm(data=request.POST)
#
#         if form.is_valid():
#             password1, password2 = form.cleaned_data.get('password1'), form.cleaned_data.get('password2')
#             if password1 == password2:
#                 User.objects.create_user(
#                     username=form.cleaned_data.get('username'),
#                     password=form.cleaned_data.get('password1')
#                 )
#                 return redirect('/users/login/')
#             else:
#                 form.add_error('password1', 'Paroli ne sovpadayut')
#
#         return render(request, 'users/register.html', context={
#             'form': form
#         })

class RegisterView(ListView, CreateView):
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        context = {
            'form': RegisterForm
        }
        return render(request, 'users/register.html', context=context)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            password1, password2 = form.cleaned_data.get('password1'), form.cleaned_data.get('password2')
            if password1 == password2:
                User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                return redirect('/users/login/')
            else:
                form.add_error('password1', 'Paroli ne sovpadayut')

        return render(request, 'users/register.html', context={
            'form': form
        })
