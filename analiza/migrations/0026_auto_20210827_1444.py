# Generated by Django 3.2.6 on 2021-08-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analiza', '0025_auto_20210827_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rachunki',
            name='kwota',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rachunki',
            name='waluta',
            field=models.CharField(choices=[('EUR', 'EUR'), ('PLN', 'PLN')], default='', max_length=4),
        ),
    ]
