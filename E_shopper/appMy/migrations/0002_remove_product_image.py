# Generated by Django 4.1.5 on 2023-03-29 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
