from django.urls import path
from .views import post_list, post_detail
app_name = 'forumapp'
urlpatterns = [
    path('', post_list, name = 'post_list'),
    path('<slug:get_slug>/<int:get_id>', post_detail, name = 'post_details'),
]