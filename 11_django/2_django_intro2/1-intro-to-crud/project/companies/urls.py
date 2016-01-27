from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'companies.views.index', name='index'),
]