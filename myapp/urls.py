from django.urls import path
from django.views.generic import TemplateView
from myapp import views


urlpatterns = [
    path('index', TemplateView.as_view(template_name='index.html'), name='index'),
    path('cacique', TemplateView.as_view(template_name='cacique.html'), name='cacique'),
    path('megamall', TemplateView.as_view(template_name='megamall.html'), name='megamall'),
    path('laquinta', TemplateView.as_view(template_name='laquinta.html'), name='laquinta'),
    path('cuartaetapa', TemplateView.as_view(template_name='cuartaetapa.html'), name='cuartaetapa'),
    path('caracoli', TemplateView.as_view(template_name='caracoli.html'), name='caracoli'),
    path('laflorida', TemplateView.as_view(template_name='laflorida.html'), name='laflorida'),
    path('delacuesta', TemplateView.as_view(template_name='delacuesta.html'), name='delacuesta'),
    path('', views.lista_centros_comerciales, name='lista_centros_comerciales'),
    path('tiendas', views.lista_tiendas, name='lista_tiendas'),
]