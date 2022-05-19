from django.db import models


class Category(models.Model):
    name = models.CharField("Категория", max_length=60,)
    url = models.SlugField(max_length=150, unique=True)
            
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class IceFatContent(models.Model):
    fat_content = models.CharField("Жирность", max_length=60, blank=True)
    url = models.SlugField(max_length=150, unique=True)
    class Meta:
        verbose_name = 'Жирность'
        verbose_name_plural = 'Жирности'

class Doc(models.Model):
    img = models.ImageField("Изоброжения", upload_to="movie_shots/")
    price = models.CharField("Цена", max_length=50, blank=True)
    title = models.TextField("Название", max_length=250, blank=True)
    desc = models.TextField("Описание", max_length=500, blank=True)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    fat_content = models.ManyToManyField(IceFatContent, verbose_name="Жирность")
    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженые'

