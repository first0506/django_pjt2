from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.review_list, name='index'),
    path('create/', views.create_review, name='create'),
    path('<int:review_pk>/', views.review_detail, name='detail'),
    path('<int:review_pk>/update/', views.update_review, name='update'),
    path('<int:review_pk>/delete/', views.delete_review, name='delete'),
]