# Generated by Django 4.1.5 on 2023-04-06 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0004_alter_userinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(default='product/img6.jfif', upload_to='product', verbose_name='Profil Resmi'),
        ),
    ]