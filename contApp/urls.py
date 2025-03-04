from django.urls import path
from .views import ContactCreateAPIView,ContactDeatilsView

# Create your urls here.
urlpatterns = [
    path('create/',ContactCreateAPIView.as_view(),name='create'),
    path('update/<int:pk>/',ContactDeatilsView.as_view(),name='update'),
    path('delete/<int:pk>/',ContactDeatilsView.as_view(),name='delete'),
]