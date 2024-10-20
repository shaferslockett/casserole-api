from django.urls import path
from .views import CasseroleList, CasseroleDetail, ObtainApiKeyView

urlpatterns = [
    path('casseroles/', CasseroleList.as_view(), name='casserole-list'),
    path('casseroles/<str:name>/', CasseroleDetail.as_view(), name='casserole-detail'),
    path('auth/', ObtainApiKeyView.as_view(), name='obtain-api-key'),
]