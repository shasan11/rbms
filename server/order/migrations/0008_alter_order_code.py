# Generated by Django 3.2.5 on 2023-02-26 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='Rbvk7', max_length=5, unique=True, verbose_name='Order No'),
        ),
    ]
