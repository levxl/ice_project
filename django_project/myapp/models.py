from django.db import models

class Doc(models.Model):
    img = models.ImageField("Изоброжения", upload_to="movie_shots/")
    price = models.CharField("Цена", max_length=50, blank=True)
    title = models.TextField("Название", max_length=250, blank=True)
    desc = models.TextField("Описание", max_length=500, blank=True)

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженые'

class IceFatContent(models.Model):
    fat_content = models.CharField("Жирность", max_length=60, blank=True)

    class Meta:
        verbose_name = 'Жирность'
        verbose_name_plural = 'Жирности'