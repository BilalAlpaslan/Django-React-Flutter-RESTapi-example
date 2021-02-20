from django.db import models


class Article(models.Model):
	id = models.AutoField(primary_key=True)
	slug = models.CharField(max_length=100, verbose_name='slug')
	author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar ",related_name="article")
	name = models.CharField(max_length=100, verbose_name='Başlık')
	description = models.CharField(max_length=1000, verbose_name='Yazı')
	image = models.FileField(blank = True,null = True, verbose_name='Başlık Resmi')
	created_date = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-created_date']
