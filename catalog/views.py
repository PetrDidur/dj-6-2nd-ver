from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    

class ContactsView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} {email} {message}')
        return render(request, self.template_name)


def card(request):
    return render(request, 'catalog/card.html')
