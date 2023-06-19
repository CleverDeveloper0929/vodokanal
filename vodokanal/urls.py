"""vodokanal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main.views import ListLics, detail_lics, ListDom, DetailDom, ListNasPunkt, DetailNasPunkt, \
    ListPersons, DetailPersons, ListKvartiry, DetailKvartiry, ListStreets, DetailStreets, \
    ListLgoty, DetailLgoty, ListTipLgoty, DetailTipLgoty, ListPribory, DetailPribory, \
    ListMarkiPribory, DetailMarkiPribory, ListUslugi, DetailUslugi

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ListLics.as_view(), name='index'),

    # lics
    url(r'^lics/$', ListLics.as_view(), name='list_lics'),
    url(r'^lics/(?P<lics_id>[0-9]+)/$', detail_lics, name='detail_lics'),

    # dom
    url(r'^dom/$', ListDom.as_view(), name='list_dom'),
    url(r'^dom/(?P<pk>[0-9]+)/$', DetailDom.as_view(), name='detail_dom'),

    # nas_punkt
    url(r'^nas_punkt/$', ListNasPunkt.as_view(), name='list_NasPunkt'),
    url(r'^nas_punkt/(?P<pk>[0-9]+)/$', DetailNasPunkt.as_view(), name='detail_NasPunkt'),

    # persons
    url(r'^persons/$', ListPersons.as_view(), name='list_persons'),
    url(r'^persons/(?P<pk>[0-9]+)/$', DetailPersons.as_view(), name='detail_persons'),

    # kvartiry
    url(r'^kvartiry/$', ListKvartiry.as_view(), name='list_kvartiry'),
    url(r'^kvartiry/(?P<pk>[0-9]+)/$', DetailKvartiry.as_view(), name='detail_kvartiry'),

    # Streets
    url(r'^streets/$', ListStreets.as_view(), name='list_streets'),
    url(r'^streets/(?P<pk>[0-9]+)/$', DetailStreets.as_view(), name='detail_streets'),

    # lgoty
    url(r'^lgoty/$', ListLgoty.as_view(), name='list_lgoty'),
    url(r'^lgoty/(?P<pk>[0-9]+)/$', DetailLgoty.as_view(), name='detail_lgoty'),

    # tip_lgoty
    url(r'^tip_lgoty/$', ListTipLgoty.as_view(), name='list_tip_lgoty'),
    url(r'^tip_lgoty/(?P<pk>[0-9]+)/$', DetailTipLgoty.as_view(), name='detail_tip_lgoty'),

    # pribory
    url(r'^pribory/$', ListPribory.as_view(), name='list_pribory'),
    url(r'^pribory/(?P<pk>[0-9]+)/$', DetailPribory.as_view(), name='detail_pribory'),

    # Marki priborov
    url(r'^marki_pribory/$', ListMarkiPribory.as_view(), name='list_marki_pribory'),
    url(r'^marki_pribory/(?P<pk>[0-9]+)/$', DetailMarkiPribory.as_view(), name='detail_marki_pribory'),

    # uslugi
    url(r'^uslugi/$', ListUslugi.as_view(), name='list_uslugi'),
    url(r'^uslugi/(?P<pk>[0-9]+)/$', DetailUslugi.as_view(), name='detail_uslugi'),


]
