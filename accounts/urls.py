from django.urls import path
from .views import profileupdate

urlpatterns = [
    path('<str:name>', profileupdate, name='profileupdate')
]

app_name = "accounts"