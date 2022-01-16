from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List


class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self) -> float:
        correct_answer = {0: ['B'], 1: ['A'], 2: ['A'], 3: ['C', 'D'], 4: ['A', 'C']}
        percent = 0.0
        return percent
