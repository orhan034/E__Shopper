# Generated by Django 4.1.5 on 2023-04-05 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0002_alter_userinfo_deneyim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='deneyim',
            field=models.IntegerField(default=0, verbose_name='Deneyim'),
        ),
    ]
