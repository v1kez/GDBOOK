from django.contrib.auth.forms import UserCreationForm

from .models import Book, Reviews
from django.forms import ModelForm, TextInput, FileInput, Textarea


class BookForm(ModelForm):

    class Meta:
        # Название модели на основе
        # которой создается форма
        model = Book
        # Включаем все поля с модели в форму
        fields = ['name_book', 'description_book', 'author_book', 'file', 'photo']

        widgets = {
            "name_book": TextInput(attrs={
                'class': 'create-form-input create-input-name',
                'type': "text",
                'name': "bookName",
                'placeholder':  "name book"
            }),
            "description_book": TextInput(attrs={
                'class': 'create-form-input create-input-description',
                'type': "text",
                'name': "bookDescription",
                'placeholder':  "description book"
            }), "author_book": TextInput(attrs={
                'class': 'create-form-input create-input-author',
                'type': "text",
                'name': "bookAuthor",
                'placeholder':  "author book"
            }), "file": FileInput(attrs={
                'class': 'form-control',
                'type': "file",
                'name': "file",
            }), "photo": FileInput(attrs={
                'class': 'form-control',
                'type': "file",
                'name': "photo"
            })

        }

class ReviewsForm(ModelForm):

    class Meta:
        # Название модели на основе
        # которой создается форма
        model = Reviews
        # Включаем все поля с модели в форму
        fields = ['nickname', 'reviews']

        widgets = {
            "nickname": TextInput(attrs={
                'class': 'create-form-input create-input-name',
                'type': "text",
                'placeholder': 'USERNAME',

            }),
            "reviews": Textarea(attrs={
                'class': 'form-control',
                'placeholder':'REVIEWS',

            })

        }




class RegForm(UserCreationForm):
    pass