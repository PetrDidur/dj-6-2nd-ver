from django.core.management import BaseCommand

from catalog.models import Category


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


