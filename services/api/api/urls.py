from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from records import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('records.urls')),
]
