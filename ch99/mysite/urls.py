from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import HomeView
from .views import UserCreateView, UserCreateDoneTV

urlpatterns = [
                path('admin/', admin.site.urls),
                path('accounts/', include('django.contrib.auth.urls')),
                path('accounts/register/', UserCreateView.as_view(), name='register'),
                path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
                # shkim
                path('', HomeView.as_view(), name='home'),
                path('bookmark/', include('bookmark.urls')),
                path('blog/', include('blog.urls')),
                path('photo/', include('photo.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

