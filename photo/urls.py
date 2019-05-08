from django.urls import path
from .views import PhotoList, PhotoCreate, PhotoDetail, PhotoUpdate, PhotoDelete

app_name = 'photo'

urlpatterns = [
    path('', PhotoList.as_view(), name='index'),
    path('create/', PhotoCreate.as_view(), name='create'),
    path('detail/<int:pk>/', PhotoDetail.as_view(), name='detail'),
    path('update/<int:pk>/', PhotoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PhotoDelete.as_view(), name='delete'),


]