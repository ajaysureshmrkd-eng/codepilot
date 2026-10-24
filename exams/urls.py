from django.urls import path

from exams.views import AssementListView
from exams.views import AssementCreateView
from exams.views import AssementRetrieveUpdateDeleteView
# from exams.views import AssementRetrieveUpdateDeleteView


urlpatterns = [

    path("all/",AssementListView.as_view()),
    path("add/",AssementCreateView.as_view()),
    path('<int:pk>/',AssementRetrieveUpdateDeleteView.as_view()),
    # path("assements/<int:pk>/",AssementRetrieveUpdateDeleteView.as_view()),
]