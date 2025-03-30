# Generated by Django 5.1.7 on 2025-03-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userpayment_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpayment',
            name='payment_method',
            field=models.CharField(choices=[('card', 'Картка'), ('cash', 'Готівка'), ('Рахунок', 'iban')], default='card', max_length=10, verbose_name='Метод платежу'),
        ),
    ]
