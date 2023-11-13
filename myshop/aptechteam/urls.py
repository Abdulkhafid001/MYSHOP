from django.urls import path
# import view module to invoke our views
from . import views
urlpatterns = [
    path("", views.members, name='aptechteam'),
    path('playerdetail/<int:player_id>', views.detail_view, name='details'),
    # this url patterns are for testing the images
    path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.image_list, name='image_list'),
]