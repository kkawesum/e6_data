from django.urls import path
from .views import BlogView, get_all,get_one


urlpatterns = [
    path('all/', get_all),
    path('id/<int:pk>', get_one),
    path('blog/', BlogView.as_view()),
]
