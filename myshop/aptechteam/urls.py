from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# import view module to invoke our views
from . import views
urlpatterns = [
    path("", views.members, name='aptechteam'),
    path('playerdetail/<int:player_id>', views.detail_view, name='details'),
    # this url patterns are for testing the images
    path('upload/', views.upload_image, name='upload_image'),
    path('images/<int:img_id>', views.image_list, name='image_list'),
]
# settings to get the media folder
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
