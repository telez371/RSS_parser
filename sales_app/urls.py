"""
URL configuration for sales_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.urls import path

from rss_handler.admin import admin_site
from rss_handler.views import admin_login, dashboard, manage_rss_feeds, toggle_rss_feed_status, delete_rss_feed


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin_login, name='admin_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/add_rss_feed/', dashboard, name='add_rss_feed'),
    path('dashboard/add_gpt_prompt/', dashboard, name='add_gpt_prompt'),
    path('dashboard/add_google_chat/', dashboard, name='add_google_chat'),
    path('dashboard/add_telegram/', dashboard, name='add_telegram'),
    path('dashboard/add_fibery/', dashboard, name='add_fibery'),
    path('manage-rss/', manage_rss_feeds, name='manage_rss_feeds'),
    path('toggle-rss/<int:pk>/', toggle_rss_feed_status, name='toggle_rss_feed_status'),
    path('delete-rss/<int:pk>/', delete_rss_feed, name='delete_rss_feed'),

]



