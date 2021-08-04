
from django.contrib import admin
from django.urls import path, include
from .views import home_page
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('', include('administration.urls')),
    path('teacher/', include('teacher.urls')),
    path('student/', include('student.urls')),
    path('academic/', include('academic.urls')),
    path('employee/', include('employee.urls')),
    path('result/', include('result.urls')),
    path('address/', include('address.urls')),
    path('account/', include('account.urls')),
    path('attendance/', include('attendance.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
