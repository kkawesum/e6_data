from django.urls import path
from .views import BlogView, PublicBlog,get_one


urlpatterns = [
    path('all/', PublicBlog.as_view()),
    path('id/<int:pk>', get_one),
    path('blog/', BlogView.as_view()),
]
