from django.contrib import admin
from django.urls import path, include

from bookmark.views import BookmarkLV, BookmarkDV
# from bookmark.views import *


urlpatterns = [
    path('admin/', admin.site.urls),


    # class-based views
    # path('bookmark/', include('bookmark.urls'))

    path('bookmark/', BookmarkLV.as_view(), name = 'index'),
    path('bookmark/<int:pk>/', BookmarkDV.as_view(), name = 'detail'),
]
