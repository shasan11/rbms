# Generated by Django 3.2.5 on 2023-02-26 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_auto_20230226_1123'),
        ('core', '0003_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Branch', to='branch.branch', verbose_name='Branch'),
        ),
    ]
