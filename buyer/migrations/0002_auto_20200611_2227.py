# Generated by Django 2.2 on 2020-06-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='product_name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]