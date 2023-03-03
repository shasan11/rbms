# Generated by Django 3.2.5 on 2023-02-26 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('branch', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCharge',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Charge Name')),
                ('type_charge', models.CharField(choices=[('A', 'Amount'), ('P', 'Percent')], max_length=100, verbose_name='Type')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Discount Charge',
                'verbose_name_plural': 'Discount Charges',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(default='FM5VM', editable=False, max_length=5, unique=True, verbose_name='Bill No')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='branch.branch', verbose_name='Branch')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.order', verbose_name='Order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Billed By')),
            ],
            options={
                'verbose_name': 'Sales',
            },
        ),
        migrations.CreateModel(
            name='ServiceCharge',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Charge Name')),
                ('type_charge', models.CharField(choices=[('A', 'Amount'), ('P', 'Percent')], max_length=100, verbose_name='Type')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Service Charge',
                'verbose_name_plural': 'Service Charges',
            },
        ),
        migrations.CreateModel(
            name='TaxCharge',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Charge Name')),
                ('type_charge', models.CharField(choices=[('A', 'Amount'), ('P', 'Percent')], max_length=100, verbose_name='Type')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Tax Charge',
                'verbose_name_plural': 'Tax Charges',
            },
        ),
        migrations.CreateModel(
            name='SalesItems',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=100, verbose_name='Item')),
                ('qty', models.PositiveIntegerField(verbose_name='Quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Unit Price')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total')),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='billing.sales', verbose_name='Sales')),
            ],
            options={
                'verbose_name': 'Sale Items',
            },
        ),
        migrations.CreateModel(
            name='SalesCharges',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Charge Name')),
                ('c_feild', models.CharField(choices=[('D', 'Discount'), ('S', 'Service'), ('T', 'Taxes')], max_length=100, verbose_name='Type')),
                ('type_charge', models.CharField(choices=[('A', 'Amount'), ('P', 'Percent')], max_length=100, verbose_name='Type')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Value')),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='billing.sales', verbose_name='Sales')),
            ],
            options={
                'verbose_name': 'Sale Charges',
            },
        ),
        migrations.CreateModel(
            name='SalesAmount',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Discount')),
                ('add_charge', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Additional Charges')),
                ('taxable', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Taxable Amount')),
                ('taxes', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Taxes')),
                ('gtotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Grand Total')),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='billing.sales', verbose_name='Sales')),
            ],
            options={
                'verbose_name': 'Sales Amounts',
            },
        ),
    ]
