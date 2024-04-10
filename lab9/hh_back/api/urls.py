from django.urls import path
from .views import *

urlpatterns = [
    path('companies/', get_all_companies),
    path('companies/<int:pk>/', get_company),
    path('companies/<int:pk>/vacancies', get_vacancies_by_company),
    path('vacancies/', get_all_vacancies),
    path('vacancies/<int:pk>/', get_vacancy),
    path('vacancies/top_ten/', get_top_ten_vacancies),
    path('', get_error_page),
]