# Generated by Django 3.2.6 on 2021-08-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analiza', '0019_alter_rachunki_kwota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rachunki',
            name='kwota',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100000, null=True),
        ),
        migrations.AlterField(
            model_name='rachunki',
            name='waluta',
            field=models.CharField(choices=[('PLN', 'PLN'), ('EUR', 'EUR')], default='', max_length=4),
        ),
    ]
