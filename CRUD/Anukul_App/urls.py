from django.urls import path
from Anukul_App import views

urlpatterns = [
path('',views.home),
path('Love',views.Love),
path('Laugh',views.Laugh),
path('Angry',views.Angry),
path('user_inp',views.user_inp)
]