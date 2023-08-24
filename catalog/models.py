from django.conf import settings
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
    creation_date = models.DateField(verbose_name='дата изготовления', auto_now_add=True)
    last_change_date = models.DateField(verbose_name='дата изменения', auto_now_add=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')


    def __str__(self):
        return f'{self.name}, {self.price_for_purchase}, {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, max_length=100, verbose_name='product')
    version_number = models.FloatField(verbose_name='версия номер')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    is_active = models.BooleanField(default=False, verbose_name='текущая версия')

    def __str__(self):
        return f'{self.product} {self.version_number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версия'



