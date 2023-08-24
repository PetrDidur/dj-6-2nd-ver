from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Version
from catalog.forms import ProductForm, VersionForm


class ProductListView(ListView):
    model = Product


class ContactsView(View):
    template_name = 'catalog/contacts_detail'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} {email} {message}')
        return render(request, self.template_name)


@method_decorator(login_required(login_url='users:register'), name='dispatch')
class CardDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        versions = Version.objects.filter(product=context['product'])

        context['versions'] = versions
        return context


@method_decorator(login_required(login_url='users:register'), name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


@method_decorator(login_required(login_url='users:register'), name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description','category', 'price_for_purchase')

    def get_success_url(self):
        return reverse('view_product', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


@method_decorator(login_required(login_url='users:register'), name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('homepage')








