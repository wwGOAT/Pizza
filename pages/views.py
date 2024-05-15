from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import ProductModel


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        pizza = ProductModel.objects.filter(category__name='pizza')
        burger = ProductModel.objects.filter(category__name='burger')
        salad = ProductModel.objects.filter(category__name='salad')
        drinks = ProductModel.objects.filter(category__name='drinks')
        fries = ProductModel.objects.filter(category__name='fries')
        context = {
            'pizza': pizza,
            'burger': burger,
            'salad': salad,
            'drinks': drinks,
            'fries': fries
        }
        return context