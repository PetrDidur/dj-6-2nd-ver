from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product/', verbose_name='изображение/превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=100, verbose_name='категория')
    price_for_purchase = models.IntegerField(verbose_name='цена за покупку')
    creation_date = models.DateField(verbose_name='дата изготовления')
    last_change_date = models.DateField(verbose_name='дата изменения', auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.price_for_purchase}, {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

