# Generated by Django 3.2.5 on 2023-02-26 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
        ('order', '0017_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='JfrN3', editable=False, max_length=5, unique=True, verbose_name='Order No'),
        ),
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='table_name', to='table.tablename', verbose_name='Table'),
        ),
    ]
