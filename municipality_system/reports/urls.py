from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_issue, name='report'),
    path('track/', views.track_issue, name='track'),
]