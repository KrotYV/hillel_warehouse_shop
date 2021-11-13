from django.urls import include, path
from django.views.generic import TemplateView

from .views import RegisterFormView
from . import views

urlpatterns = [
    path('register/', RegisterFormView.as_view(), name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='index'),
    path('catalog/', views.BooksView.as_view(), name='posts'),
    path('genre/', views.GenreView.as_view(), name='genre'),
]