# Generated by Django 3.2.5 on 2023-02-26 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableCategory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='category Name')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch.branch', verbose_name='Branch')),
            ],
            options={
                'verbose_name': 'Table',
                'verbose_name_plural': 'Tables',
            },
        ),
        migrations.CreateModel(
            name='TableName',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Table Name')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('tcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.tablecategory', verbose_name='Table Category')),
            ],
            options={
                'verbose_name': 'Table',
                'verbose_name_plural': 'Tables',
            },
        ),
    ]
