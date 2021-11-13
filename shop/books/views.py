from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegisterForm
from .models import Book, Genre


class RegisterFormView(generic.FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()

        username = self.request.POST['username']
        password = self.request.POST['password1']

        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)


class BooksView(generic.ListView):
    model = Book
    paginate_by = 20
    template_name = 'books_list.html'


class GenreView(generic.ListView):
    model = Genre
    template_name = 'genre_list.html'