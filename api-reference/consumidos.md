---
layout: page
title: Consumidos
---

## Ir a

1. [Modelos](#modelos)
* [Vistas](#vistas)
* [Formas](#formas)


## Modelos

**expedientedental.consumidos.models**

### `Paquete`
Los Paquetes se usan para agrupar Productos necesarios para realizar un 'servicio' o 'procedimiento'. Facilita el proceso de la persona en inventario. Deben ser creados previamente y se necesita familarizacion con los 'servicios' o 'procedimientos'.

Atributos:

* `nombre = models.CharField(max_length=50, unique=True)`
* `descripcion = models.CharField(max_length=200)`
* `productos = models.ManyToManyField('inventario.Producto', through='PaqueteItem')`
* `is_inactive = models.BooleanField(default=False)`

### `CancelPaquete`

Hereda de `expedientedental.core.models.CancelledModel`.

El crear este modelo indica que el paquete en el `ForeignKey` esta desactivado. Se provee motivo y se agrega fecha de creacion.

Atributos:

* `paquete = models.ForeignKey(Paquete)`

### `PaqueteItem`

Productos de un paquete.

Atributos:

* `paquete = models.ForeignKey(Paquete)`
* `producto = models.ForeignKey('inventario.Producto')`
* `cantidad_producto = models.DecimalField(max_digits=8, decimal_places=2)`

### `PaqueteConsumido`

Indica un grupo de productos que saldran de inventario.

Atributos:

* `paquete = models.ForeignKey(Paquete, null=True)`
* `medico = models.ForeignKey(Medico)`
* `paciente = models.ForeignKey(Paciente)`
* `servicio = models.ForeignKey('servicios.Servicio', null=True)`
* `nota = models.TextField(blank=True)`
* `status = models.CharField()` - contiene 'choices'.

Metodos:

* `get_item_initials` - Asigna initials usando PaqueteItems con ForeignKey a Paquete.
* `precio_total` - Saca el total de todos los PaqueteConsumidoItems con ForeignKey a PaqueteConsumido.

### `CancelPaqueteConsumido`

Hereda del modelo abstracto CancelledModel (`expedientedental.core.CancelledModel`) que contiene 'motivo' y 'created_at'. Agrega relacion con la salida a cancelar.

### `PaqueteConsumidoItemManager`

Metodos:

* `get_precio_total` - Suma el precio de PaqueteConsumidoItem.

### `PaqueteConsumidoItem`

Producto a salir de inventario. Contiene el precio de acorde al precio del producto y la cantidad que va de salida (se consume).

Atributos:

* `paquete_consumido = models.ForeignKey(PaqueteConsumido)`
* `producto = models.ForeignKey('inventario.Producto')`
* `cantidad = models.DecimalField(max_digits=8, decimal_places=2)`
* `precio = models.DecimalField(max_digits=8, decimal_places=2)`

Methods:

* `set_precio` - Calcula el precio correcto a asignar multiplicando el precio del producto por la cantidad de este.

## Vistas

**expedientedental.consumidos.views**

### `Paquetes`

Lista de paquetes.

Hereda de:

* **django.views.generic.ListView**

### `PaqueteCreate`

Crea un objeto Paquete con PaqueteItems. La magia esta en la forma!

Hereda de:

* **django.views.generic.CreateView**

### `PaqueteDetail`

Muestra detalle de paquete y da la opcion de marcar como 'surtido'.

Hereda de:

* **django.views.generic.UpdateView**

### `PaqueteCancel`

Pagina de confirmacion para agregar `CancelPaquete`. Aqui se escribe el motivo de cancelacion y se marca como cancelado el paquete.

Hereda de:

* **expedientedental.core.CreateObjFromContext**

### `PaqueteCancelled`

Lista de paquetes cancelados.

Hereda de:

* **django.views.generic.ListView**

### `PaqueteCancelledDetail`

Detalle de paquete cancelado. Es del  modelo `CancelPaquete`. Muestra motivo, los items y todo lo demas.

Hereda de:

* **django.views.generic.DetailView**

### `PaqueteUpdate`

TODO: en la segunda iteracion. Requiere trabajo en la forma.

Hereda de:

* **django.views.generic.UpdateView**

### `Peticiones`

Lista de peticiones o `PaqueteConsumido`. Muestra los `PaqueteConsumido` con estatus de `en_espera` y `por_entregar` en dos listas independientes.

Hereda de:

* **django.views.generic.ListView**

### `PeticionCreate`

Crea `PaqueteConsumido` con paquete nulo. Define el `Paquete` a partir del `Servicio`. Con el metodo `get_initial` define tambien el `Medico` y el `Paciente` a partir del `Servicio`.

Hereda de:

* **expedientedental.core.views.CreateObjFromContext**

### `PeticionUpdate`

Agrega `Paquete` a `PaqueteConsumido`.

Hereda de:

* **django.views.generic.UpdateView**

### `PeticionesAtendidas`

Lista de peticiones o `PaqueteConsumido` con estatus de `surtido`.

Hereda de:

* **django.views.generic.ListView**

### `paquete_item_create`

Crea `PaqueteConsumidoItem`s de `PaqueteItem`s y agrega o quita items extra (productos).

### `PeticionDetail`

Detalle de `PaqueteConsumido` con sus items (`PaqueteConsumidoItem`). Tiene la posibilidad de marcar `PaqueteConsumido` como `surtido`. Al marcar como surtido, se restan los productos de inventario.

Hereda de:

* **django.views.generic.UpdateView**

### `PeticionCancel`

Vista de confirmacion para cancelar una peticion o crear un `CancelPaqueteConsumido`. Devuelve los productos a inventario.

Hereda de:

* **expedientedental.core.views.CreateObjFromContext**

### `PeticionCancelled`

Lista de peticiones canceladas o `CancelPaqueteConsumido`.

Hereda de:

* **django.views.generic.ListView**

### `ReciboPeticionPDF`

Recibo de la peticion de materiales.

Hereda de:

* **wkhtmltopdf.views.PDFTemplateView**

## Formas

**expedientedental.consumidos.forms**

### `PaqueteForm`

Crea `Paquete` con `PaqueteItem`s basado en los productos disponibles (activos).

Hereda de:

* **django.forms.ModelForm**

### `PaqueteCancelForm`

Forma con solo el campo de `is_inactive`. Es un foreshadower a la cancelacion del paquete. No guarda los cambios al objeto.

Hereda de:

* **django.forms.ModelForm**

### `CancelPaqueteForm`

Crea `CancelPaquete` y modifica tambien el modelo de `Paquete`, cuyo valor viene en el initial.

Hereda de:

* **django.forms.ModelForm**

### `PeticionForm`

Crea `PaqueteConsumido` con `Paquete` nulo. Asigna valores de `medico`, `paciente` y `servicio` a partir del initial.

Hereda de:

* **django.forms.ModelForm**

### `AtenderPeticionForm`

Agrega `Paquete` a `PaqueteConsumido`.

Hereda de:

* **django.forms.ModelForm**

### `PaqueteItemCreateForm`

Crea `PaqueteConsumidoItem`s a partir de `PaqueteItem`s en `Paquete` y agrega o quita items (productos) extra. No muestra productos que no se encuentren en existencia en inventario o que esten desactivados.

Hereda de:

* **django.forms.ModelForm**

### `PeticionSurtidoForm`

Cambia el estatus de `PaqueteConsumido` de `por_entregar` a `surtido` y vice versa.

Hereda de:

* **django.forms.ModelForm**

### `PeticionCancelForm`

Crea `CancelPaqueteConsumido`.

Hereda de:

* **django.forms.ModelForm**
