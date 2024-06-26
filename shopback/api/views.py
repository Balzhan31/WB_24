from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Category, Product

# Create your views here.

def get_epmty_page(request):
    return HttpResponse('<h1>Error! Page not found</h1>')

def get_categories(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def get_category(request, pk=None):
    try:
        category = Category.objects.get(id=pk)
        return JsonResponse(category.to_json())
    except Category.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
        }, status=404)


def get_products(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def get_product(request, pk=None):
    try:
        product = Product.objects.get(id=pk)
        return JsonResponse(product.to_json())
    except Category.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
        }, status=404)


def get_products_by_category(request, categ_id=None):
    try:
        category = Category.objects.get(id=categ_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=404)

    products = Product.objects.filter(category_id=categ_id)
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)