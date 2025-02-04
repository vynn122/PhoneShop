from django.urls import path
from .import views
urlpatterns =[
    path('', views.homepage, name='homepage'),
    path('all-phones/', views.all_phones, name='all_phones'),
    path('about/', views.about, name='about'),
    path('login/',views.login_customer, name='loginpage'),
    path('register/',views.register_customer, name="register"),
    path("logout/", views.logout_customer, name="logout"),

]