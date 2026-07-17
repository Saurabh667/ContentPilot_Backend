from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from media import views
from media.process import updateRecord
from media.process import getGeneratedClips

urlpatterns = [
    path('upload/', views.upload_video, name='upload_video'),
    path('videos/', views.get_user_videos, name='get_videos'),
    path("updateRecord/", updateRecord),
    path("generatedClips/", getGeneratedClips),
    # path('videos/<int:id>/', views.delete_video, name='delete_video'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
