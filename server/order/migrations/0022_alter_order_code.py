# Generated by Django 3.2.5 on 2023-02-26 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_auto_20230226_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='A6KDi', editable=False, max_length=5, unique=True, verbose_name='Order No'),
        ),
    ]
