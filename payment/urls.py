from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donate_page, name="donate_page"),
    path('payment-success/', views.payment_success, name="payment_success"),
]
