# Generated by Django 3.2.5 on 2023-02-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0027_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='37ssb', editable=False, max_length=5, unique=True, verbose_name='Order No'),
        ),
    ]
