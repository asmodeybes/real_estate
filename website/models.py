from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta




class Category(models.Model):
    # Здесь достаточно CharField на 50-60 символов
    name = models.CharField(max_length=50, verbose_name="Категория")

    class Meta:
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Destrict(models.Model):
    # Здесь достаточно CharField на 50-60 символов
    name = models.CharField(max_length=50, verbose_name="Район")

    class Meta:
        verbose_name_plural = "Районы"

    def __str__(self):
        return self.name


class Operation(models.Model):
    # Здесь достаточно CharField на 50-60 символов
    name = models.CharField(max_length=50, verbose_name="Тип операции")

    class Meta:
        verbose_name_plural = "Тип операции"

    def __str__(self):
        return self.name





class Ad(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", default=2)

    # Здесь должна быть связь ForeignKey
    #area = models.ForeignKey(Destrict, verbose_name="Район")
    district = models.ForeignKey(Destrict, verbose_name="Район", default=1)
    operation=models.ForeignKey(Operation, verbose_name="Тип операции", default=2)
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = models.TextField(max_length=400, verbose_name="Текст объявления")
    price = models.IntegerField(verbose_name="Цена, $", default=0)
    rooms= models.IntegerField(verbose_name="Количество комнат", default=0)
    total_area=models.IntegerField(verbose_name="Общая площадь, м.кв.", default=0)
    living_area = models.IntegerField (verbose_name="Жилая площадь м.кв.", default=0)
    area=models.IntegerField (verbose_name="Площадь м.кв.", default=0)
    kitchen_area= models.IntegerField(verbose_name="Площадь кухни м.кв.", default=0)
    floor= models.IntegerField(verbose_name="Этаж", default=0)
    floors=models.IntegerField(verbose_name="Этажность дома", default=1)
    published_date = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")
    dt =models.DateTimeField(verbose_name="Дата окончания публикации")
    author = models.ForeignKey(User, verbose_name="Автор")
    # Здесь нужно CharField на 15-20 символов

    phone = models.CharField(max_length=40, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Электронная почта")
    image=models.ImageField(upload_to='website/photos', verbose_name='Фото')




    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

class Search(models.Model):
        category = models.ForeignKey(Category, verbose_name="Категория", default=0)
        district = models.ForeignKey(Destrict, verbose_name="Район", default=0)
        operation = models.ForeignKey(Operation, verbose_name="Тип операции", default=0)
        price_start = models.IntegerField(verbose_name="Цена от, $", default=0)
        price_finish = models.IntegerField(verbose_name="Цена до, $", default=0)
        rooms = models.IntegerField(verbose_name="Количество комнат", default=0)

        def __str__(self):
            return self.title

        class Meta:
            verbose_name = "Search"
            verbose_name_plural = "Search"




# class Photo(models.Model):
#     ad = models.ForeignKey(Ad)
#     image = models.ImageField('Фото ', upload_to='upload/images')
