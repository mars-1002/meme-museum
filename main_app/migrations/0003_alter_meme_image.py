# Generated by Django 4.2.2 on 2023-06-06 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_meme_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='image',
            field=models.CharField(max_length=250),
        ),
    ]
