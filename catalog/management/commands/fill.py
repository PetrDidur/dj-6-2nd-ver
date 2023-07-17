from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):

        categories_list = [
            {'name': 'footwear', 'description': 'Good'},
            {'name': 'clothes', 'description': 'Good1'},
            {'name': 'accessories', 'description': 'Good2'},
            {'name': 'pants', 'description': 'Good3'},
        ]
        categories_for_create = []

        for category_item in categories_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categories_for_create)

        product_list = [{ "name": "Sneakers", "description": "good for walking", "category": Category.objects.get(pk=1),
                         "price_for_purchase": 1000, "creation_date": "2023-07-04",
                          "last_change_date": "2023-07-17"}]


        products_to_create = []

        for product_item in product_list:
            products_to_create.append(
                Product(**product_item)
            )
        Product.objects.bulk_create(products_to_create)




