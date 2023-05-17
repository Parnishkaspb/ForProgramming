from django.db import models
from django.urls import reverse
# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=100, verbose_name='Вопрос')
    type = models.ForeignKey('Types', on_delete=models.PROTECT, verbose_name='Тип')

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Types(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Тип')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Тип'

class Answer(models.Model):
    answer = models.CharField(max_length=100, verbose_name='Ответ')
    rightanswer = models.BooleanField(default=False, verbose_name='Правильный ответ')
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='Вопрос')

    def __str__(self):
        return self.answer
    
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
    