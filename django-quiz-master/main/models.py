from django.db import models


class Question(models.Model):
    title = models.TextField('Name')  # text of question

    def __str__(self):
        return self.title


class Answers(models.Model):
    answer_A = models.TextField('description')
    answer_B = models.TextField('description')
    answer_C = models.TextField('description')
    answer_D = models.TextField('description')

    def __str__(self):
        return self.answer_A

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
