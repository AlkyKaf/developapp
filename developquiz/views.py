from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserResponse


def index(request):
    quizzes = Quiz.objects.filter(is_ready_to_publish=True)
    context = {"quizzes": quizzes}
    return render(request, "index.html", context=context)


@login_required(login_url='login')
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    context = {"quiz": quiz, "questions": questions}
    return render(request, "quiz_detail.html", context)


@login_required(login_url='login')
def quiz_submit(request, quiz_id):
    count = 0
    if request.method == "POST":
        quiz = get_object_or_404(Quiz, id=quiz_id)
        questions = quiz.questions.all()
        error_message = None
        for question in questions:
            choice_id = request.POST.get(f"question_{question.id}", None)
            if choice_id:
                choice = get_object_or_404(Choice, id=choice_id)
                UserResponse.objects.create(
                    user=request.user,
                    quiz=quiz,
                    question=question,
                    selected_choice=choice
                )

                for j in Question.objects.filter(quiz_id=quiz_id):
                    if j == question:
                        if j.choices.all().filter(score=1).get() == choice:
                            count += 1


            else:
                error_message = "you need select answers"

        if error_message:
            context = {"quiz": quiz, "questions": questions}
            return render(request, "quiz_detail.html", context)

        print(f'{count} questions answered')
        context = {"count": count, "total_count": len(questions)}
        return render(request, "result.html", context=context)
    return redirect("quiz_detail", quiz_id=quiz_id)
