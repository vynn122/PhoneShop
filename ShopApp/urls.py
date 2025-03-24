from django.urls import path
from .import views
from .views import *
urlpatterns =[
    path('', views.homepage, name='homepage'),
    path('all-phones/', views.all_phones, name='all_phones'),
    path('Apple/', views.brand_iphone, name='brand_iphone'),
    path('Samsung/', views.brand_samsung, name='brand_samsung'),
    path('Oppo/', views.brand_oppo, name='brand_oppo'),
    path('Vivo/', views.brand_vivo, name='brand_vivo'),
    path('phone/<int:product_id>/', views.single_product, name='single_product'),
    path('about/', views.about, name='about'),
    path('login/',views.login_customer, name='loginpage'),
    path('register/',views.register_customer, name="register"),
    path("logout/", views.logout_customer, name="logout"),
	path('update_item/', views.updateItem, name="update_item"),
    path("checkout/", checkout, name="checkout"),
    path("success/", success_page, name="checkout_success"),
    path("cf_checkout/", views.cf_checkout, name="cf_checkout"),
    path("user_info", views.user_page, name="user_info"),

]