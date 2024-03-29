from django.urls import path, include
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, PostFilterView


urlpatterns = [
        path('', PostsList.as_view()),
        path('<int:pk>',PostDetail.as_view()),
        path('search/', PostFilterView.as_view()),
              ]