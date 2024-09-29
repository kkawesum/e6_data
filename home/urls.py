from django.urls import path
from .views import BlogView, get_all


urlpatterns = [
    path('all/', get_all),
    path('blog/', BlogView.as_view()),
]
