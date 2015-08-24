from django.conf.urls import include, url
from django.contrib import admin
from web.views import HomeTemplateView , ProfesorListView , ServicioTemplateView , RevistaListView ,\
 RecursoTemplateView , ContactFormView , PanelView , ContenidoUpdateView , RevistaUpdateView , ModuloUpdateView ,\
 NivelUpdateView , ContenidoCreateView , RevistaCreateView , NivelCreateView , ProfesorUpdateView ,\
 ProfesorCreateView , ProListView , ProfesorDetailView

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profesores/$', ProfesorListView.as_view(), name='profesores'),
    url(r'^servicios/$', ServicioTemplateView.as_view(), name='servicios'),
    url(r'^revista/$' , RevistaListView.as_view(), name='revista' ),
    url(r'^recursos/$', RecursoTemplateView.as_view(), name='recursos'),
    url(r'^contacto/$', ContactFormView.as_view() , name='contacto'),
    url(r'^panel/$', PanelView.as_view() , name='panel'),
    url(r'^contenido/(?P<pk>\d+)/editar/$' , ContenidoUpdateView.as_view() , name='editC'),
    url(r'^revista/(?P<pk>\d+)/editar/$' , RevistaUpdateView.as_view() , name='editR'),
    url(r'^modulo/(?P<pk>\d+)/editar/$' , ModuloUpdateView.as_view() , name='editM'),
    url(r'^nivel/(?P<pk>\d+)/editar/$' , NivelUpdateView.as_view() , name='editN'),
    url(r'^contenido_create/$', ContenidoCreateView.as_view() , name='c_create'),
    url(r'^revista_create/$', RevistaCreateView.as_view() , name='r_create'),
    url(r'^nivel_create/$', NivelCreateView.as_view() , name='n_create'),
    url(r'^pro/(?P<pk>\d+)/editar/$' , ProfesorUpdateView.as_view() , name='editPro'),
    url(r'^pro_create/$' , ProfesorCreateView.as_view() , name='p_create'),
    url(r'^edit_pro/$' , ProListView.as_view() , name='pro_edit'),
    url(r'^login/' , 'django.contrib.auth.views.login' , { 'template_name' : 'login.html'  }) ,
    url(r'^profesor/(?P<pk>\d+)/detail/$', ProfesorDetailView.as_view(), name='profesor-detail'),
]


