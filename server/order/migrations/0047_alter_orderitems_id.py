# Generated by Django 3.2.5 on 2023-03-01 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0046_auto_20230228_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]