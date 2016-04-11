from django.conf.urls import url,patterns
from whoismuhammad import views

urlpatterns = patterns('',
			url(r'^$', views.index, name='index')
			)

