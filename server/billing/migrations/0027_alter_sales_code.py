# Generated by Django 3.2.5 on 2023-02-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0026_alter_sales_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='code',
            field=models.CharField(default='TasdS', editable=False, max_length=5, unique=True, verbose_name='Bill No'),
        ),
    ]
