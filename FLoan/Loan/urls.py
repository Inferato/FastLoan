from django.urls import path
from . import views

app_name = 'Loan'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('profile/', views.main_page, name='main_page')
]
