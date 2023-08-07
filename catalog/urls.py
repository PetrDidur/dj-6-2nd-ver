from django.urls import path

from catalog.views import card, ProductListView, ContactsView

urlpatterns = [
    path('', ProductListView.as_view(), name='homepage'),
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('card', card)
]
