from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'article.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'contact/$','article.views.contact', name='contact'),
    url(r'calculate/$','article.views.calculate', name='calculate'),
    url(r'clients_data/(?P<pk>\d+)$','article.views.clients_data', name='clients_data'),
    url(r'report/$','article.views.report', name='report'),
    url(r'report2/$','article.views.report2', name='report2'),
    url(r'date/$','article.views.date', name='date'),
    url(r'fetch/$','article.views.fetch', name='fetch'),
    url(r'^download/(?P<pk>\d+)$', 'article.views.download',name='download'),
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
