# Generated by Django 4.2.3 on 2023-07-20 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_change_date',
            field=models.DateField(auto_now_add=True, verbose_name='дата изменения'),
        ),
    ]
