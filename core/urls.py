from django.contrib import admin
from django.urls import path
from climatempo.views import WeatherView

urlpatterns = [
    path('', WeatherView.as_view()),
    path('admin/', admin.site.urls),
]
