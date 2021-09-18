"""mikesplayground_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from pages.views import home_view, css_view, regex_view, chuck_view, estonia_view, germany_view, russia_view, library_view, graphs_view, parsing_view, lightbox_view
from blog.views import blogpost_list_view, dynamic_lookup_view, blogpost_delete_view, blogpost_create_view, blogpost_edit_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('database/', blogpost_list_view, name="database"),
    path('database/<int:id>/', dynamic_lookup_view, name="blogpost-detail"),
    path('database/<int:id>/delete/', blogpost_delete_view, name="blogpost-delete"),
    path('database/create/', blogpost_create_view, name="blogpost-create"),
    path('database/<int:id>/edit/', blogpost_edit_view, name="blogpost-edit"),
    path('blogpost_list/', blogpost_list_view, name="blogpost-list"),
    path('regex/', regex_view, name="regex"),
    path('lightbox', lightbox_view, name="lightbox"),
    # path('socials', socials_view, name="socials"),
    path('chuck_norris/', chuck_view, name="chuck"),
    path('parsing', parsing_view, name="parsing"),
    path('css/', css_view, name="css"),
    path('graphs/', graphs_view, name="graphs"),
    path('estonia/', estonia_view, name="estonia"),
    path('germany/', germany_view, name="germany"),
    path('russia/', russia_view, name="russia"),
    path('imperial_library', library_view, name="imperial_library"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
