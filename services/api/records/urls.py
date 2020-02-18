from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^records/(?P<pk>[0-9]+)$',
        views.get_delete_update_record,
        name='get_delete_update_record'
    ),
    url(
        r'^records/$',
        views.get_post_records,
        name='get_post_records'
    )
]
