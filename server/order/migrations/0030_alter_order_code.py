# Generated by Django 3.2.5 on 2023-02-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0029_auto_20230226_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='Mz5E7', editable=False, max_length=5, unique=True, verbose_name='Order No'),
        ),
    ]
