from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def home_view(request):
    slides = Slider.objects.all()
    context = {'slides':slides}
    return render(request,'homepage.html',context)

def menu_list(request):
    pass
    return render(request,'menus.html')
def menu_items(request, slug=None):
    if slug is None:
        # If no category slug is provided, display all menu items
        menu_items = MenuItem.objects.all()
        context = {"menu_items": menu_items}
    else:
        # If a category slug is provided, filter menu items by category
        categories = get_object_or_404(MenuCategory, slug=slug)
        menu_items = MenuItem.objects.filter(categories=categories)
        context = {"categories": categories, "menu_items": menu_items}
    return render(request, 'menus.html', context)
