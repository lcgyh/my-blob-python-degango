from django.urls import path
from . import views

app_name='blob'
urlpatterns = [
    path('',views.index),
    path('articles/<int:article_id>/',views.articel_page,name="article_page"),
    path('edit/<int:article_id>/',views.edit_page,name="edit_page"),
    path('edit/action/',views.edit_action,name="edit_action"),
]
