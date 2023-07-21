from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def index_homepage(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'main/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} {email} {message}')
    return render(request, 'main/contacts.html')


def card(request):
    return render(request, 'main/card.html')
