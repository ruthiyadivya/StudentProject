from django.contrib import admin
from django.urls import path
from app1.views import home
from app2.views import sample_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('sample/', sample_page, name='sample_page'),
]
