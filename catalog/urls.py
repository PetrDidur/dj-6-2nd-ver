from django.urls import path

from catalog.views import ProductListView, ContactsView, CardDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='homepage'),
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('view/<int:pk>/', CardDetailView.as_view(), name='view')
]
