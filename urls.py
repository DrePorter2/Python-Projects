from django.contrib import admin
from django.urls import path
# mapping url patterns for routing
urlpatterns = [
    path('admin/', admin.site.urls),
]