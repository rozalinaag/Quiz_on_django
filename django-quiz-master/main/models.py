from django.db import models


class Question(models.Model):
    title = models.TextField('Name')  # text of question

    def __str__(self):
        return self.title


class ChoiceDTO(models.Model):
    text = models.TextField('choice')
    is_correct = models.BooleanField('is correct')

    def __str__(self):
        return self.text


class QuestionDTO(models.Model):
    text = models.TextField('question')
    choices = list([ChoiceDTO])

    def __str__(self):
        return self.text


class QuizDTO(models.Model):
    title = models.TextField('title')
    questions = list([QuestionDTO])

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


class AnswerDTO(models.Model):
    question_uuid = models.ForeignKey(QuestionDTO, on_delete=models.CASCADE)
    choices = list([str])


class AnswersDTO(models.Model):
    quiz_uuid = models.ForeignKey(QuizDTO, on_delete=models.CASCADE)
    answers = list([AnswerDTO])
