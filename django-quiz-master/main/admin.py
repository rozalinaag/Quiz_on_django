from django.contrib import admin
from .models import Question, Answers, ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO


admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(ChoiceDTO)
admin.site.register(QuestionDTO)
admin.site.register(QuizDTO)
admin.site.register(AnswerDTO)
admin.site.register(AnswersDTO)
