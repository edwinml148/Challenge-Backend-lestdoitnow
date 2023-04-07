from inventory.serializers.movements import MovementsSerializer
from inventory.exceptions import (
    MovementsEntryParameterIsRequired,
    ProductDetailsParameterIsRequired1,
    ProductDetailsParameterIsRequired2,
    LotParameterIsRequired,
    CustomersDoesNotExist,
    ProductDoesNotExist,
    CustomerWithoutUser,
    WarehouseAdminWithoutWarehouse,
    UncreatedPossibleProductsOnWarehouses,
    ProductsOnWarehousesDoesNotExist,
    ThereAreNotEnoughProductsInStock,
)
from inventory.models.customers import Customers
from inventory.models.products import Products 
from inventory.models.warehouses_admins import Warehouse_admin
from inventory.models.products_movements import Movements
from inventory.models.products_movements_description import Movements_description
from inventory.models.lot_description import Lot_description
from inventory.models.products_on_warehouses import Products_on_warehouses


def validate_movements_entry(remission, description, customer, products_details):
    if bool(remission) and bool(description) and not(customer is None) and bool(products_details):
        for product_details in products_details:
            if "product" in product_details.keys() and "description" in product_details.keys() and "lot" in product_details.keys() and "product_qty" in product_details.keys(): 
                if  "lot_id" in product_details["lot"] and "due_date" in product_details["lot"] and "product" in product_details["lot"] :
                    validate_customer(customer)
                    validate_product(product_details["lot"]["product"])
                else: raise LotParameterIsRequired 
            else: raise ProductDetailsParameterIsRequired1
    else: raise MovementsEntryParameterIsRequired


def validate_movements_exit(remission, description, customer, products_details):
    if bool(remission) and bool(description) and not(customer is None) and bool(products_details):
        for product_details in products_details:
            if "product" in product_details.keys() and "description" in product_details.keys() and "product_qty" in product_details.keys(): 
                validate_customer(customer)
            else: raise ProductDetailsParameterIsRequired2
    else: raise MovementsEntryParameterIsRequired


def validate_customer(customer):
    customers = Customers.objects.filter(id=customer).exists()
    if not customers:
        raise CustomersDoesNotExist


def validate_product(product):
    product = Products.objects.filter(id=product).exists()
    if not product:
        raise ProductDoesNotExist


def get_user_and_warehouse_from_customer(customer):
    customers = Customers.objects.filter(id=customer).first()
    user = customers.user
    if not user:
        raise CustomerWithoutUser
    warehouse_admin = Warehouse_admin.objects.filter(user_id=user).first()
    warehouse = warehouse_admin.warehouse
    if not warehouse:
        raise WarehouseAdminWithoutWarehouse
    return user, warehouse, customers


def get_product_from_details(product):
    products = Products.objects.filter(id=product).first()
    return products


def get_lots_enabled_ordered_by_expiration(product_id, warehouse):
    products_on_warehouses = get_products_on_warehouses(product_id, warehouse.id, None)
    if not products_on_warehouses:
        raise ProductsOnWarehousesDoesNotExist
    lots_enabled = []
    for product_on_warehouses in products_on_warehouses:
        lot_id=product_on_warehouses.lot.lot_id
        lot_description = Lot_description.objects.filter(lot_id=lot_id).first()
        lots_enabled.append((product_on_warehouses.id,lot_description, product_on_warehouses.stock, lot_description.due_date))

    # Ordenamos la data de forma descendente respecto a la fecha de caducidad del lote
    lots_enabled_sort = sorted(lots_enabled, key = lambda x : x[3])
    return lots_enabled_sort


def get_lots_discount_products(lots_enabled,product_qty):
    validation_total_products_in_stock(lots_enabled, product_qty)
    chosen_lots = []
    for lot_enabled in lots_enabled:
        quantity_products_in_lot = lot_enabled[2]
        chosen_lots.append([lot_enabled[0],lot_enabled[1],quantity_products_in_lot])
        if product_qty - quantity_products_in_lot< 0:
            chosen_lots[-1][2] = product_qty
            break
        product_qty = product_qty - quantity_products_in_lot
    return chosen_lots


def validation_total_products_in_stock(lots_enabled, product_qty):
    product_total = 0
    for lot in lots_enabled:
        product_total = product_total + lot[2]
    if product_total < product_qty:
        raise ThereAreNotEnoughProductsInStock
    

def get_or_create_lot_from_details(lot,product):
    lot_id = lot["lot_id"]
    due_date = lot["due_date"]
    product = lot["product"]
    lot_description = Lot_description.objects.filter(
        lot_id=lot_id,
        due_date=due_date,
        product=product).first()
    if not lot_description:
        parameters = {
            "lot_id":lot_id,
            "due_date":due_date,
            "product":get_product_from_details(product),
        }
        lot_description = Lot_description(**parameters)
        lot_description.save()
    return lot_description


def get_products_on_warehouses(product_id, warehouse_id, lot_id):
    if lot_id:
        products_on_warehouses = Products_on_warehouses.objects.filter(
            product=product_id,
            warehouse=warehouse_id,
            lot=lot_id
            ).first()
    else:
        products_on_warehouses = Products_on_warehouses.objects.filter(
            product=product_id,
            warehouse=warehouse_id
            ).all()
    return products_on_warehouses


def get_movements_from_customer(customer):
    movements_object = Movements.objects.filter(customer_id=customer).all()
    movements = [MovementsSerializer(movement).data for movement in movements_object]
    return movements


def create_movements(remission, description, customer,movement_type):
    user, warehouse, customers  = get_user_and_warehouse_from_customer(customer)
    parameters = {
        "warehouse":warehouse,
        "movement_type":movement_type,
        "description":description,
        "user":user,
        "remission":remission,
        "customer":customers
    }
    movement = Movements(**parameters)
    movement.save()
    return movement, warehouse


def create_movements_description(lot, product, movement,product_qty,description, movement_type):
    if movement_type == "entry":
        lot_object = get_or_create_lot_from_details(lot,product)
    if movement_type == "exit":
        lot_object = Lot_description.objects.filter(lot_id=lot).first()
        
    parameters = {
        "movement":movement,
        "product":product,
        "product_qty":product_qty,
        "description":description,
        "lot":lot_object
    }
    movement_description = Movements_description(**parameters)
    movement_description.save()
    return movement_description, lot_object


def update_products_on_warehouses(movement, products_details, warehouse, movement_type):
    movements_descrip = []
    detail_ = ""
    for product_details in products_details:
        product_qty = product_details["product_qty"]
        product_id = product_details["product"]
        product = get_product_from_details(product_id)
        lot = product_details.get("lot")
        description = product_details["description"]

        if lot:
            movement_description, lot_object = create_movements_description(lot, product, movement,product_qty,description, movement_type)
            movements_descrip.append(movement_description.id)
            update_or_create_products_on_warehouses(product, product_qty, warehouse, lot_object, movement_type)   
        else:
            lots_enabled_sort = get_lots_enabled_ordered_by_expiration(product_id, warehouse)
            chosen_lots = get_lots_discount_products(lots_enabled_sort,product_qty)
            for chosen_lot in chosen_lots:
                if chosen_lot[2] != 0:
                    product_qty = chosen_lot[2]
                    movement_description, lot_object = create_movements_description(chosen_lot[1].lot_id, product, movement, product_qty,description, movement_type)
                    movements_descrip.append(movement_description.id)
                    detail = update_or_create_products_on_warehouses(product, product_qty, warehouse, lot_object, movement_type)
                    detail_ = detail_ + "  " + detail
    return movements_descrip, detail_


def create_products_on_warehouses(product, product_qty, warehouse, lot):
    parameters = {
        "product":product,
        "stock":product_qty,
        "warehouse":warehouse,
        "lot":lot
    }
    products_on_warehouses = Products_on_warehouses(**parameters)
    products_on_warehouses.save()


def update_or_create_products_on_warehouses(
    product,
    product_qty,
    warehouse,
    lot,
    movement_type
    ):
    detail = ""
    products_on_warehouses = get_products_on_warehouses(product.id, warehouse.id, lot.lot_id)
    if movement_type == "entry":
        if products_on_warehouses:
            products_on_warehouses.stock = products_on_warehouses.stock + product_qty
            products_on_warehouses.save()
        else:
            create_products_on_warehouses(product, product_qty, warehouse, lot)
    elif movement_type == "exit":
        if products_on_warehouses:
            products_on_warehouses.stock = products_on_warehouses.stock - product_qty
            products_on_warehouses.save()
            if products_on_warehouses.stock==0:
                detail = f"Se acabo el producto {product.name} con el lote {lot.lot_id}"
        else:
            raise UncreatedPossibleProductsOnWarehouses
    return detail
