# Generated by Django 4.1.5 on 2023-04-06 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0003_alter_userinfo_deneyim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(default='product/img6.jfif', upload_to='', verbose_name='Profil Resmi'),
        ),
    ]