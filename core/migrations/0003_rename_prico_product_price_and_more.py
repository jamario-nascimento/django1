# Generated by Django 4.2.6 on 2023-10-08 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_client_product_delete_produto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prico',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='estoque',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
