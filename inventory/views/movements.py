from rest_framework.response import Response
from inventory.filters import *
from rest_typed_views import typed_api_view, Body
from rest_framework import status
from inventory.schemas.movements import ProductsDetailsSchema
from inventory.services.movements import (
    validate_movements_entry,
    create_movements,
    update_products_on_warehouses,
    validate_movements_exit,
    get_movements_from_customer
)
from typing import Optional


@typed_api_view(['POST'])
def v1_movements_entry(
    remission: Optional[str] = Body(source='remission', default=""),
    description: Optional[str] = Body(source='description', default=""),
    customer: Optional[int] = Body(source='customer', default=None),
    products_details: Optional[ProductsDetailsSchema] = Body(source='products_details', default= [])
    ) -> Response:
    movement_type = "entry"
    validate_movements_entry(remission, description, customer, products_details)
    movement, warehouse = create_movements(remission, description, customer, movement_type)
    movements_descripcion, __ = update_products_on_warehouses(movement, products_details, warehouse, movement_type)
    return Response(
        {
            "status": "Done",
            "movement_id": movement.id,
            "movements_descripcion":movements_descripcion
        }
        , status=status.HTTP_200_OK)


@typed_api_view(['POST'])
def v1_movements_exit(
    remission: Optional[str] = Body(source='remission', default=""),
    description: Optional[str] = Body(source='description', default=""),
    customer: Optional[int] = Body(source='customer', default=None),
    products_details: Optional[ProductsDetailsSchema] = Body(source='products_details', default= [])
    ) -> Response:
    movement_type = "exit"
    validate_movements_exit(remission, description, customer, products_details)
    movement, warehouse = create_movements(remission, description, customer, movement_type)
    movements_descripcion, detail = update_products_on_warehouses(movement, products_details, warehouse, movement_type)
    return Response(
        {
            "status": "Done",
            "movement_id": movement.id,
            "movements_descripcion":movements_descripcion,
            "detail": detail
        }
        , status=status.HTTP_200_OK)


@typed_api_view(['GET'])
def v1_movements(customer: Optional[int]) -> Response:
    movements = get_movements_from_customer(customer)
    return Response({ 'data' : movements }, status=status.HTTP_200_OK)
