from django.urls import path

from catalog.views import ProductListView, ContactsView, CardDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='homepage'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('view/<int:pk>/', CardDetailView.as_view(), name='view_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

]
