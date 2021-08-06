from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.example),
    path('webhooks/', views.webhooks),
    path('webhookstest/', views.webhookstest)

]
