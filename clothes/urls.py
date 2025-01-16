from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    GarmentListView,
    PublishGarmentView,
    UnpublishGarmentView,
    UpdateGarmentView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', GarmentListView.as_view(), name='garment_list'),
    path('publish/', PublishGarmentView.as_view(), name='publish_garment'),
    path('<int:pk>/unpublish/', UnpublishGarmentView.as_view(), name='unpublish_garment'),
    path('<int:pk>/update/', UpdateGarmentView.as_view(), name='update_garment'),

]
