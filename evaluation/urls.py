from django.urls import path
from evaluation.views import SubmissionCreateView
from evaluation.views import AnswercreateView
from evaluation.views import SubmissionRetrieveView
from evaluation.views import AnswerUpdateView

urlpatterns =[
    path("assessment/<int:pk>/submission/",SubmissionCreateView.as_view()),

    path("submission/<int:pk>/answer/",AnswercreateView.as_view()),

    path("submission/<int:pk>/",SubmissionRetrieveView.as_view()),

    path("answer/<int:pk>/",AnswerUpdateView.as_view()),
]