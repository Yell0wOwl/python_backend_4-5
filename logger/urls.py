"""application URL Configuration

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
from . import views
from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import MessageViewSet

router_messages = DefaultRouter()
router_messages.register(r'api/messages', MessageViewSet, basename='messages')

routers = [router_messages]

urlpatterns = [
]

for single_router in routers:
    urlpatterns += single_router.urls

# urlpatterns = [
#     path('', views.log_index, name='log_index'),
#
#     path('<slug:companion_id>/msg_create',
#          views.msg_create, name='message_create'),
#     path('<int:id>/msg_info', views.msg_info, name='message_info'),
#     path('msg_list', views.msg_list, name='message_list'),
#     path('<int:id>/msg_change', views.msg_change, name='message_change'),
#     path('<int:id>/msg_delete', views.msg_delete, name='message_delete'),
# ]
