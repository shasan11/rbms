# Generated by Django 3.2.5 on 2023-03-01 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0047_auto_20230228_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalCharges',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Charge Name')),
                ('type_charge', models.CharField(choices=[('A', 'Amount'), ('P', 'Percent')], max_length=100, verbose_name='Type')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Value')),
                ('default_charge', models.BooleanField(default=True, verbose_name='Default Charge')),
            ],
            options={
                'verbose_name': 'Additional Charge',
                'verbose_name_plural': 'Additional Charges',
            },
        ),
        migrations.CreateModel(
            name='Taxation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Charge Name')),
                ('type_charge', models.CharField(choices=[('A', 'Amount'), ('P', 'Percent')], max_length=100, verbose_name='Type')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Value')),
                ('default_charge', models.BooleanField(default=True, verbose_name='Default Charge')),
            ],
            options={
                'verbose_name': 'Tax Charge',
                'verbose_name_plural': 'Tax Charges',
            },
        ),
        migrations.RemoveField(
            model_name='payments',
            name='pmethod',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='sid',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='user',
        ),
        migrations.DeleteModel(
            name='ServiceCharge',
        ),
        migrations.DeleteModel(
            name='PaymentMethod',
        ),
        migrations.DeleteModel(
            name='Payments',
        ),
    ]
