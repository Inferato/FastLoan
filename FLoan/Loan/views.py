from django.contrib.auth import login, authenticate
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .form import UserForm, SignUpForm


def main_page(request):
    return render(request, 'Loan/main.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('Loan:main_page')
    else:
        form = SignUpForm()
    return render(request, 'Loan/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('Loan:main_page')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login or password{}'.format(user))
    else:
        form = UserForm()
    return render(request, 'Loan/signin.html', {'form': form})
