# Generated by Django 3.1.1 on 2020-09-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baajaar_app', '0003_auto_20200928_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
