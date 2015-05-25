from django.conf.urls import include, url
from django.contrib import admin
from web.views import HomeTemplateView , ProfesorListView

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profesores', ProfesorListView.as_view(), name='profesores'),
]
