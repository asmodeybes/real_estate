from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.TextField(verbose_name="Категория")

    class Meta:
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Destrict(models.Model):
    name = models.TextField(verbose_name="Район")

    class Meta:
        verbose_name_plural = "Районы"

    def __str__(self):
        return self.name




class Ad(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория")

    area = models.OneToOneField(Destrict, verbose_name="Район")
    title = models.CharField(max_length=40, verbose_name="Заголовок")
    content = models.TextField(max_length=400, verbose_name="Текст объявления")
    price = models.IntegerField(verbose_name="Цена", default=0)
    published_date = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")
    author = models.ForeignKey(User, default=User.objects.get(pk=1))
    phone=models.IntegerField(verbose_name="Телефон", default=0000000000)
    email=models.EmailField(verbose_name="Электронная почта")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


# class Photo(models.Model):
#     ad = models.ForeignKey(Ad)
#     image = models.ImageField('Фото ', upload_to='upload/images')

