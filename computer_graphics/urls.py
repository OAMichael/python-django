"""
URL configuration for computer_graphics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('',                  views.index),
    path('functions-list-gl', views.functions_list, {"api": views.api_functions_work.API_TYPE_GL}),
    path('functions-list-vk', views.functions_list, {"api": views.api_functions_work.API_TYPE_VK}),
    path('add-function-gl',   views.add_function, {"api": views.api_functions_work.API_TYPE_GL}),
    path('add-function-vk',   views.add_function, {"api": views.api_functions_work.API_TYPE_VK}),
    path('send-function-gl',  views.send_function, {"api": views.api_functions_work.API_TYPE_GL}),
    path('send-function-vk',  views.send_function, {"api": views.api_functions_work.API_TYPE_VK}),
    path('statistics',        views.statistics),
    path('feedback',          views.user_feedback),
    path('send-feedback',     views.send_feedback)
]
