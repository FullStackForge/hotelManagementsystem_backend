from django.urls import path
from . import views
urlpatterns = [
    path('roomtypes/', views.RoomTypeListView.as_view()),
    path('roomtypes/<str:uuid>', views.RoomTypeDetailView.as_view())
]
