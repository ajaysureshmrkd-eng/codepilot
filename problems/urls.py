from django.urls import path,include

from problems.views import QuestionCreateView
from problems.views import RetrieveUpdateDeleteView

urlpatterns = [
   path("assessment/<int:pk>/question/",QuestionCreateView.as_view()),
   path("ret/upd/del/<int:pk>/",RetrieveUpdateDeleteView.as_view()),


    
]