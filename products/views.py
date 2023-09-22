from django.shortcuts import render
from django.views import generic

from .models import Product


class ShoppingList(generic.ListView):
    model = Product
    paginate_by = 2
    template_name ='products/shop_list.html'
    context_object_name = 'productslist'


class ListDetail(generic.DetailView):
    model = Product
    template_name = 'products/detail_list.html'
    context_object_name = 'detaillist'


# class CommentViews(generic.ListView):
#     model = Comment
#     template_name = 'products/detail_list.html'
#     context_object_name = 'comments'

