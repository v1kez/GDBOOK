from django.urls import path
from . import views
from .views import BookCreate, Registration

urlpatterns = [
    path('', views.index),
    path('reviews', views.reviews),
    path('book/', views.book),
    # path('sign', views.sign),
    path('add_reviews', views.add_reviews),
    path('create/', BookCreate.as_view()),
    path('register/', Registration.as_view(), name='register'),
    # path('profile',profile_view,name="profile"),
    # # path('register', views.register),
    # path('login', views.login),
    path('<int:pk>/delete', views.Delete.as_view(), name='delete')
]
