from django.urls import path
from . import views

urlpatterns = [

path('', views.pos, name='pos'),
    path('receipt/<int:order_id>/', views.receipt, name='receipt'),
    path('report/', views.report, name='report'),

]