# Challenge-Backend-lestdoitnow
Prueba tecnica para la vacante de Desarrollador Backend Python

## Endpoints

### Entrada de Inventario

```
Url : http://localhost:8000/v1/customers/movements/entry
Metodo : POST
Body:
{
    "remission": "12345",
    "description": "Prueba de entradax5",
    "customer": 3,
    "products_details":[
        {
            "product": 1,
            "description": "Entrada de pruebax7",
            "product_qty": 50,
            "lot": {
                "lot_id": "ejemplo lot 1",
                "due_date": "2021-05-25",
                "product": 1
            }
        },
        {
            "product": 1,
            "description": "Hola mundo ejejej",
            "product_qty": 500,
            "lot": {
                "lot_id": "Prueba x123",
                "due_date": "2023-01-25",
                "product": 1
            }
        }
    ]
}
```

### Salida de inventario


```
Url : http://localhost:8000/v1/customers/movements/exit
Metodo : POST
Body:
{
    "remission": "12345",
    "description": "retiro de almacen",
    "customer": 3,
    "products_details":[
        {
            "product": 1,
            "description": "Soy una prueba",
            "product_qty": 600
        }
    ]
}
```


### Historial de movimientos


```
Url : http://localhost:8000/v1/customers/<int:customer>/movements
Metodo : GET

```

### Consideraciones:
* Se muestran excepciones en caso la estructura del body para los metodos post no se respete
* Se muestran excepciones en caso no exista el customer y lot_product
* Para el caso de salida de inventario se retira primero los productos de los lotes mas proximos a vencer.
* Para el caso de salida de inventario no alcanza con el lote mas proximo a vencer, se sigue con el siguiente lote a vencer.
* Hay excepciones en caso la cantidad a retirar sea superior a la cantidad total de stock
