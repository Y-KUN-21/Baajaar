# Generated by Django 3.1.1 on 2020-09-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baajaar_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product/'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profilePic',
            field=models.ImageField(upload_to='profile/'),
        ),
    ]
