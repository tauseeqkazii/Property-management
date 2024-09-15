from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.list_properties, name='list_properties'),
    path('properties/<int:property_id>/tenants/', views.list_tenants, name='list_tenants'),
    path('tenants/<int:tenant_id>/payments/', views.view_payment_history, name='view_payment_history'),
    path('upload-lease-agreement/', views.upload_lease_agreement, name='upload_lease_agreement'),
    path('search/properties/', views.search_properties, name='search_properties'),
    path('search/tenants/', views.search_tenants, name='search_tenants'),
]
