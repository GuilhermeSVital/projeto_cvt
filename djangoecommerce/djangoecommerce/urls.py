"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from core import views
from core.views import index

""" lista de URLS do meu Sistema, cada url é um padrão"""
"^ significa o início de uma string, $ significa o fechamento dessa instring, se nao tem nada no meio é a url mãe, a inicial do nosso site "
"o segundo parametro passado na url é a nossa view, que nesse primeiro caso é o 'index"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cursos/$', views.cursos_list, name='cursos'),
    url(r'^curso/$', views.curso, name='curso'),
    url(r'^contato/$', views.contato, name='contato'),
    url(r'^admin/', admin.site.urls),

]
