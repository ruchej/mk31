# -*- coding: utf-8 -*-


from django.db import models
from mk31 import settings
import os


class CategoryFurniture(models.Model):
    '''Таблица категорий мебели: кухни, шкафы и т.п.
    category_name - название категории: кухни, шкафы...
    folder_name - имя папки картинок категории'''
    
    category_name = models.CharField(max_length=50, verbose_name='Категория')
    folder_name = models.CharField(max_length=50, verbose_name='Папка')
    
    class Meta:
        verbose_name = 'Категорию мебели'
        verbose_name_plural = 'Категории мебели'
    
    def __str__(self):
        return self.category_name

class FurnitureProduct(models.Model):
    '''Мебельное изделие. Для каждой категории вписывается своё изделие
        со своими характеристиками'''
    category = models.ForeignKey(CategoryFurniture, on_delete=models.CASCADE, verbose_name='Категория')
    furnproduct = models.CharField(max_length=100, verbose_name='Изделие')
    
    class Meta:
        verbose_name = 'Мебельное изделие'
        verbose_name_plural = 'Мебельные изделия'
    
    def __str__(self):
        return self.furnproduct

class Images(models.Model):
    '''Таблица путей изображений'''
    furnproduct = models.ForeignKey(FurnitureProduct, on_delete=models.CASCADE, verbose_name='Изделие')
    fol = "images"
    #fol = CategoryFurniture._meta.get_field('folder_name')
    imagepath = models.ImageField(upload_to=fol, verbose_name='Изображение')
    #initpath = imagepath.path
    #imagepath.name = 'images/123.jpg'
    #new_path = settings.MEDIA_ROOT + imagepath.name
    #os.rename(initpath, new_path)
    #imagepath.path = new_path
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

