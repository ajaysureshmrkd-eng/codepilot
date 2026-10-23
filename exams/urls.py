from rest_framework.urls import path

from exams.views import AssementListCreateView
from exams.views import AssementRetrieveUpdateDeleteView


urlpatterns = [

    path("assement/",AssementListCreateView.as_view()),
    path("assements/<int:pk>/",AssementRetrieveUpdateDeleteView.as_view()),
]