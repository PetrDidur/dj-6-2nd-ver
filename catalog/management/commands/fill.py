from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories_list = [
            {'name': 'lapty', 'description': 'Good'},
            {'name': 'lapty1', 'description': 'Good1'},
            {'name': 'lapty2', 'description': 'Good2'},
            {'name': 'lapty3', 'description': 'Good3'},
        ]
        categories_for_create = []

        for category_item in categories_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categories_for_create)

        product_list = [
            {'name': 'lapty', 'description': 'Good', 'category': 'footwear',
             'price_for_purchase': '1', 'creation_date': '23.01.2000' },
            {'name': 'lapty1', 'description': 'Good1', 'category': 'footwear1', 'price_for_purchase': '11',
             'creation_date': '23.01.2001'}
        ]

        products_to_create = []

        for product_item in product_list:
            products_to_create.append(
                Product(**product_item)
            )
        Product.objects.bulk_create(products_to_create)




