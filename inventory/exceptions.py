from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException
from inventory.constants import (
    ExceptionsParameterIsRequired,
    DoesNotExist,
    Customers,
    WarehouseAdmin,
    UncreatedPossible,
    ThereAreNotEnough,
)


class MovementsEntryParameterIsRequired(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _(ExceptionsParameterIsRequired.MOVEMENTS_ENTRY)
    default_code = ExceptionsParameterIsRequired.MOVEMENTS_ENTRY


class ProductDetailsParameterIsRequired1(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _(ExceptionsParameterIsRequired.PRODUCT_DETAILS_1)
    default_code = ExceptionsParameterIsRequired.PRODUCT_DETAILS_1


class ProductDetailsParameterIsRequired2(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _(ExceptionsParameterIsRequired.PRODUCT_DETAILS_2)
    default_code = ExceptionsParameterIsRequired.PRODUCT_DETAILS_2


class LotParameterIsRequired(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _(ExceptionsParameterIsRequired.LOT)
    default_code = ExceptionsParameterIsRequired.LOT


class CustomersDoesNotExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _(DoesNotExist.CUSTOMERS_ID)
    default_code = DoesNotExist.CUSTOMERS_ID


class ProductDoesNotExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _(DoesNotExist.PRODUCTS_ID)
    default_code = DoesNotExist.PRODUCTS_ID


class CustomerWithoutUser(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _(Customers.WITHOUT_USER)
    default_code = Customers.WITHOUT_USER


class WarehouseAdminWithoutWarehouse(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _(WarehouseAdmin.WITHOUT_WAREHOUSE)
    default_code = WarehouseAdmin.WITHOUT_WAREHOUSE


class LotDoesNotExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _(DoesNotExist.LOT_ID)
    default_code = DoesNotExist.LOT_ID


class UncreatedPossibleProductsOnWarehouses(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _(UncreatedPossible.PRODUCTS_ON_WAREHOUSES)
    default_code = UncreatedPossible.PRODUCTS_ON_WAREHOUSES


class ProductsOnWarehousesDoesNotExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _(DoesNotExist.PRODUCTS_ON_WAREHOUSES_PRODUCT_ID)
    default_code = DoesNotExist.PRODUCTS_ON_WAREHOUSES_PRODUCT_ID


class ThereAreNotEnoughProductsInStock(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _(ThereAreNotEnough.PRODUCTS)
    default_code = ThereAreNotEnough.PRODUCTS
