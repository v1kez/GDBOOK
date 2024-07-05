from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import CreateView, DeleteView, FormView
from .forms import BookForm, ReviewsForm, RegForm
from .models import *


class BookCreate(CreateView):
    # Модель куда выполняется сохранение
    model = Book
    # Класс на основе которого будет валидация полей
    form_class = BookForm
    # Шаблон с помощью которого
    # будут выводиться данные
    template_name = 'main/create.html'
    # На какую страницу будет перенаправление
    # в случае успешного сохранения формы
    success_url = '/book'

class Delete(DeleteView):
    model = Book
    success_url = '/book'
    template_name ='main/delete.html'

class Registration(FormView):
    form_class = RegForm
    template_name = 'registration/register.html'
    success_url = '/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def index(request):
    return render(request,'main/index.html')

def reviews(request):
    rew = Reviews.objects.all()
    return render(request,'main/reviews.html',{ 'rew':rew })

@login_required
def book(request):
    bok = Book.objects.all()
    return render(request,'main/book.html',{ 'bok':bok })

# def sign(request):
#     return render(request,'registration/login.html')



def add_reviews(request):
    error=''
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/reviews')
        else:
            error= 'you made a mistake in filling out the form'

    form = ReviewsForm()

    data= {
        'form': form,
        'error':error
    }
    return render(request,'main/add_reviews.html', data)

# def profile_view(request):
#     return render(request,'main/sign.html')
# def registration(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # получаем имя пользователя и пароль из формы
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             # выполняем аутентификацию
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})