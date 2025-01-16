from django.urls import path

from .views import (
    GarmentListView,
    PublishGarmentView,
    UnpublishGarmentView,
    UpdateGarmentView,
)

urlpatterns = [
    path('', GarmentListView.as_view(), name='garment_list'),
    path('publish/', PublishGarmentView.as_view(), name='publish_garment'),
    path('<int:pk>/unpublish/', UnpublishGarmentView.as_view(), name='unpublish_garment'),
    path('<int:pk>/update/', UpdateGarmentView.as_view(), name='update_garment'),

]
