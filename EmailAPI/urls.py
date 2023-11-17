from django.contrib import admin
from django.urls import path
from EmailAPI.views import EmailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_email/', EmailAPIView.as_view()),
]
