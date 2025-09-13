from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register(request):
    """Регистрирует нового пользователя."""
    if request.method != 'POST':
        # Выводит пустую форму регистрации.
        form = UserCreationForm()
    else:
        # Обработка заполненной формы.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу.
            login(request, new_user)
            return redirect('tasks:index')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logout_view(request):
    """Выводит пользователя из системы."""
    logout(request)
    return render(request, 'registration/logout.html')


def login_view(request):
    """Обрабатывает вход пользователя."""
    if request.method != 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tasks:index')
    context = {'form': form}
    return render(request, 'registration/login.html', context)
