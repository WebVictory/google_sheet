# Generated by Django 4.0.4 on 2022-05-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='№')),
                ('number_order', models.IntegerField(blank=True, null=True, verbose_name='заказ №')),
                ('cost', models.FloatField(blank=True, null=True, verbose_name='стоимость,$')),
                ('delivery_time', models.DateField(blank=True, null=True, verbose_name='Срок поставки')),
                ('cost_rub', models.FloatField(blank=True, null=True, verbose_name='Стоимость в рублях')),
            ],
        ),
    ]