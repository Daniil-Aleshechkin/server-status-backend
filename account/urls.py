from django.urls import path

from account.views import (
    api_detail_account_view,
    api_register_account_view,
)
app_name = 'account'

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/register/',api_register_account_view, name="register"),
    path('api/login/',obtain_auth_token, name="login"),
    path('get',api_detail_account_view, name="get"),
]