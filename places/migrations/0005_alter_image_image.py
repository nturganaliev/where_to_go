# Generated by Django 4.2 on 2023-04-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_place_description_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Картинка'),
        ),
    ]
