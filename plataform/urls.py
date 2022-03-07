from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('immobile/<int:id>/', views.ImmobileDetailView.as_view(), name='detail'),
    path('schedule-visits/', views.schedules_visit, name='schedule-visits'),
    path('schedules/', views.SchedulesListView.as_view(), name='schedules'),
    path('cancel-schedules/<int:id>', views.cancel_schedule, name='cancel-schedules'),
]
