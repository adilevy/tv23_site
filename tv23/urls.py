"""tv23 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

import video.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^r/',video.views.view_random_video),
    url(r'^(?P<pk>\d+)/$',video.views.AssetDetailView.as_view(),name="video"),
    url(r'^$',video.views.AssetListView.as_view(),name="home"),
    url(r'^s/$',video.views.SeriesListView.as_view(),name="series_list"),
]
