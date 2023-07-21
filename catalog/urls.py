from django.urls import path

from catalog.views import index_homepage, contacts, card

urlpatterns = [
    path('', index_homepage),
    path('contacts', contacts),
    path('card', card)
]