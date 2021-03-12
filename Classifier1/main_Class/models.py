from django.db import models


class New(models.Model):  # наши новости
    tag_news = models.TextField(db_column='Tag', unique=True)
    title_news = models.TextField(db_column='Title_news', unique=True)
    text_news = models.TextField(db_column='Text_news', unique=True)

  # tag_news = models.CharField('Тег', max_length=80)
  #  title_news = models.CharField('Заголовок', max_length=120)
  #  text_news = models.TextField('Текст новости')

    def __str__(self):
        return self.title_news

    class Meta:
        managed = True
        db_table = 'texts'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


