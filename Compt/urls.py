from django.urls import path
from .import views
urlpatterns = [
    path('signup/', views.SignupViews.as_view()),
    path('login/', views.LoginViews.as_view())
]