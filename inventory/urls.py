from django.urls import path
from . import views


urlpatterns = [
    path('customers/<int:customer>/products', views.ListCreateProductGeneralAPIView.as_view(), name='get_post_products'),
    path('customers/<int:customer>/available_products', views.ListProductAvailableAPIView.as_view(), name='get_products_on_warehosue'),
    path('customers/<int:customer>/products/<int:pk>', views.RetrieveUpdateDestroyProductAPIView.as_view(), name='get_delete_update_products'),
    path('customers/movements/entry', views.v1_movements_entry, name="v1_post_movements_entry"),
    path('customers/movements/exit', views.v1_movements_exit, name="v1_post_movements_exit"),
    path('customers/<int:customer>/movements', views.v1_movements, name="v1_get_movements"),
    path('customers', views.ListCreateCustomersAPIView.as_view(), name='get_post_customers'),
    path('customers/<int:pk>', views.RetrieveUpdateDestroycustomersAPIView.as_view(), name='get_delete_update_customers'),
    path('users', views.ListUsersApiView.as_view(), name='get_users'),
    path('users/<int:pk>', views.RetrieveUpdateUserAPIView.as_view(), name='get_delete_update_user'),
    path('cities', views.ListCreateCitiesAPIView.as_view(), name='get_post_cities'),
    path('cities/<int:pk>', views.RetrieveUpdateDestroyCityAPIView.as_view(), name='get_delete_update_city'),
    path('cities/<int:city>/warehouses', views.ListCreateWarehousesAPIView.as_view(), name='get_delete_update_warehouse'),
    path('cities/<int:city>/warehouses/<int:pk>', views.RetrieveUpdateWarehouseAPIView.as_view(), name='get_delete_update_warehouse'),
    path('warehouses_admins', views.ListCreateWarehouseAdminsAPIView.as_view(), name = 'get_post_warehouse_admins'),
    path('warehouses_admins/<int:pk>', views.RetrieveUpdateDestroyWarehouseAdminAPIView.as_view(), name = 'get_delete_update_warehouse_admins'),
]