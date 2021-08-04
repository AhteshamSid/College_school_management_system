from django.urls import path
from .views import profile, update_profile

urlpatterns = [
    path('profile/<pk>/', profile, name='profile'),
    path('update/<pk>/', update_profile, name='update-profile')
]