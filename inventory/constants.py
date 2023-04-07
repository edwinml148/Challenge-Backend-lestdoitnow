
class ExceptionsParameterIsRequired:
    MOVEMENTS_ENTRY = "MOVEMENTS_ENTRY requiere los campos : remision(string), description(string), customer(integer), product_details(ProductsDetailsSchema)"
    PRODUCT_DETAILS_1 = "PRODUCT_DETAILS requiere los campos : product(integer), description(string), product_qty(integer), lot(LotSchema)"
    PRODUCT_DETAILS_2 = "PRODUCT_DETAILS requiere los campos : product(integer), description(string), product_qty(integer)"
    LOT = "LOT requiere los campos : lot_id(string), due_date(datetime), product(integer)"


class DoesNotExist:
    CUSTOMERS_ID = "No existe CUSTOMERS con ese Id"
    PRODUCTS_ID = "No existe PRODUCTS con ese Id"
    LOT_ID = "No existe LOT_DESCRIPCION con ese Id"
    PRODUCTS_ON_WAREHOUSES_PRODUCT_ID = "No existe PRODUCTS_ON_WAREHOUSES con ese product_id"


class Customers:
    WITHOUT_USER = "El customers no tiene user asignado"


class WarehouseAdmin:
    WITHOUT_WAREHOUSE = "El Warehouseadmin no tiene warehouse asignado"


class UncreatedPossible:
    PRODUCTS_ON_WAREHOUSES = "No es posible crear el registro en PRODUCTS_ON_WAREHOUSES apartir de un movimiento exits"


class ThereAreNotEnough:
    PRODUCTS = " No hay suficiente productos en stock en este almacen"