from django.conf.urls import url
from . import views

app_name = "web0"
urlpatterns = [
	# /web0/
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    # /web0/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /web0/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
]