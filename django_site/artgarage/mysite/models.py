import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Blog_post(models.Model):
	post_head = models.CharField('Заголовок поста', max_length=200)
	blog_post_text = models.TextField('Текст поста')
	pub_date = models.DateTimeField('Дата публиации')
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	def __str__(self):
		return self.post_head

class About(models.Model):
	about_text = models.TextField('Про нас')
	pub_date = models.DateTimeField('Дата публикации')
	def __str__(self):
		return about_text[0,15]