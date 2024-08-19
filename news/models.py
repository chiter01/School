from django.db import models

class News(models.Model):
    class Meta:
        verbose_name = 'новост'
        verbose_name_plural = 'новости'
    name = models.CharField(verbose_name='название', max_length=100)
    image = models.ImageField(verbose_name='изображение', upload_to='news_images/')
    description = models.CharField(verbose_name='описание', max_length=300)
    is_published = models.BooleanField(verbose_name='публичность', default=True)
    date = models.DateTimeField(verbose_name='дата добавление', auto_now_add=True)
    def __str__(self):
        return f'{self.name}'
