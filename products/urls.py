from django.urls import path
from .views import ShoppingList, ListDetail

urlpatterns = [
    path('', ShoppingList.as_view(), name='productlist'),
    path('<int:pk>/', ListDetail.as_view(), name='productdetail'),
]

