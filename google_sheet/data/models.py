from django.db import models

# По ТЗ не было ясно можно оставить форматирвание данных в формате БД
# или формат данных должен быть как в файле, если 2 то нужно все поля сделать текстового типа
# и сохранять данные как текст
# Стрктура БД
class Record(models.Model):
    number = models.IntegerField("№", blank=True,null=True)
    number_order = models.IntegerField("заказ №" ,blank=True,null=True)
    cost = models.FloatField("стоимость,$", blank=True,null=True)
    delivery_time = models.DateField("Срок поставки",blank=True,null=True)
    cost_rub = models.FloatField("Стоимость в рублях", blank=True,null=True)