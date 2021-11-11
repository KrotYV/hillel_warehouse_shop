from django.urls import include, path

from .views import RegisterFormView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterFormView.as_view(), name="register"),
]
