from django.db import models

from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField 

# Create your models here.

class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    logo = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Логотип Компании",
        blank = True, null = True
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта'
        )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    whatsapp = models.URLField(
        verbose_name='Whatspp URL',
        blank=True, null=True
    )
    whatsapp_number = models.CharField(
        max_length = 255,
        verbose_name = "Whatsapp номер"
    )
    instagram = models.URLField(
        verbose_name='Instagram URL',
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name='Youtube URL',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook URL',
        blank=True, null=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Основная настройка"
            verbose_name_plural = "Основные настройки"


class SettingsPhone(models.Model):
    settings = models.ForeignKey(Settings, related_name='phone_title', on_delete=models.CASCADE)
    phone = models.CharField(
          max_length = 255,
          verbose_name = "Телефонный номер"
     )
    class Meta:
        unique_together = ('settings', 'phone')
        verbose_name = "Дополнительный телефонный номер"
        verbose_name_plural = "Дополнительный телефонный номер"

################################################################################################################################################################################

class Category(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Заголовок"
    )
    descriptions = RichTextField(
        verbose_name="Информационный текст",
    )
    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class CategoryAdd(models.Model):
    settings = models.ForeignKey(Category,related_name = "categorys", on_delete = models.CASCADE)
    number = models.CharField(
        max_length = 255,
        default = '6',
        verbose_name = "Нумерация"
    )
    title = models.CharField(
        max_length = 255,
        verbose_name  = "Название категории"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='category/',
        verbose_name="Фотография",
        blank = False, null = False
    )
    class Meta:
        verbose_name = "Добавить категории"
        verbose_name_plural = "Добавить категории"

################################################################################################################################################################################

class Sale(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='sale/',
        verbose_name="Фотография",
        blank = False, null = False
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    descriptions = RichTextField(
        verbose_name="Информационный текст",
    )
    start_date = models.DateField(
        verbose_name="Начало",
        blank = True,null = True
    )
    end_date = models.DateField(
        verbose_name="Окончание",
        blank = True,null = True

    )
    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name = "Cкидка"
        verbose_name_plural = "Cкидки"

    
################################################################################################################################################################################

class Blog(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    descriptions = RichTextField(
        verbose_name="Информационный текст",
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='blog/',
        verbose_name="Фотография",
        blank = False, null = False
    )
    image_banner = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='blog_banner/',
        verbose_name="Фотография для баннера",
        blank = False, null = False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"