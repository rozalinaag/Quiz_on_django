from django.shortcuts import render, redirect

from quiz.dto import AnswersDTO, AnswerDTO, ChoiceDTO, QuestionDTO, QuizDTO
from .forms import QuestionForm
from .models import Question, Answers
from quiz import services

answer_user = {}


def home(request):
    if request.method == "POST":
        return redirect('question1')
    else:
        return render(request, 'main/home.html')


def question1(request):
    if request.method == "POST":
        set_answer_user(request, 1)
        return redirect('question2')
    else:
        quiz = Question.objects.filter(id=1)
        answers = Answers.objects.filter(id=1)
        return render(request, 'main/questions/question1.html',
                      {'title': 'the first question', 'my_quiz': quiz[0], 'answers_db': answers[0]})


def question2(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formOne':
            set_answer_user(request, 2)
            return redirect('question3')
        else:
            return redirect('question1')
    else:
        quiz = Question.objects.filter(id=2)
        answers = Answers.objects.filter(id=2)
        return render(request, 'main/questions/question2.html', {'title': 'the second question', 'my_quiz': quiz,
                                                                 'answers_db': answers})


def question3(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formOne':
            set_answer_user(request, 3)
            return redirect('question4')
        else:
            return redirect('question2')
    else:
        quiz = Question.objects.filter(id=3)
        answers = Answers.objects.filter(id=3)
        return render(request, 'main/questions/question3.html', {'title': 'the third question', 'my_quiz': quiz,
                                                                 'answers_db': answers})


def question4(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formOne':
            set_answer_user(request, 4)
            return redirect('question5')
        else:
            return redirect('question3')
    else:
        quiz = Question.objects.filter(id=4)
        answers = Answers.objects.filter(id=4)
        return render(request, 'main/questions/question4.html', {'title': 'the forth question', 'my_quiz': quiz,
                                                                 'answers_db': answers})


def question5(request):
    if request.method == "POST":
        if request.POST.get("form_type") == 'formOne':
            set_answer_user(request, 5)
            return redirect('results')
        else:
            return redirect('question4')
    else:
        quiz = Question.objects.filter(id=5)
        answers = Answers.objects.filter(id=5)
        return render(request, 'main/questions/question5.html', {'title': 'the fives question', 'my_quiz': quiz,
                                                                 'answers_db': answers})


def set_answer_user(request, id_question):
    answer_user[id_question - 1] = request.POST.getlist('answ')


answer_dto = AnswerDTO('', '')
choice = ChoiceDTO('', '', '')
answers_dto = AnswersDTO('', '')
question_dto = QuestionDTO('', '', '')
quiz_dto = QuizDTO('', '', '')


def results(request):
    if request.method == "POST":
        update_answer_user()
        return redirect('home')

    correct_answer = {0: ['B'], 1: ['A'], 2: ['A'], 3: ['C', 'D'], 4: ['A', 'C']}

    get_result_from_services = services.QuizResultService(quiz_dto, answers_dto)
    percent = get_result_from_services.get_result()

    for key in answer_user:
        if answer_user[key] == correct_answer[key]:
            percent += 1

    good = user_praise(percent)
    correct_mass = correctly_user_correct(correct_answer, answer_user)
    incorrect_mass = correctly_user_incorrect(correct_answer, answer_user)

    return render(request, 'main/results.html', {'result': str(percent / 5), 'good': good, 'correct': correct_mass,
                                                 'incorrect': incorrect_mass})


def user_praise(percent):
    if percent == 5:
        good = "excelente!"
    elif percent == 0:
        good = "very bad..."
    elif percent == 1:
        good = "bad :c"
    elif percent == 4:
        good = "very good!"
    elif percent == 3:
        good = "Good!"
    else:
        good = "not bad!"
    return good


def update_answer_user():
    for key in answer_user:
        answer_user[key] = 0


def correctly_user_correct(correct_answer, answers):
    correct_mass = []
    for key in answer_user:
        if answer_user[key] == correct_answer[key]:
            correct_mass.append(key + 1)
    return correct_mass


def correctly_user_incorrect(correct_answer, answers):
    incorrect_mass = []
    for key in answer_user:
        if answer_user[key] != correct_answer[key]:
            incorrect_mass.append(key + 1)
    return incorrect_mass
