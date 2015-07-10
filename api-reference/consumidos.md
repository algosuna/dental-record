---
layout: page
title: Consumidos
---

## Jump to

1. [Models](#models)
* [Views](#views)
* [Forms](#forms)


## Models

**expedientedental.consumidos.models**

### `Paquete`
Los Paquetes se usan para agrupar Productos necesarios para realizar un 'servicio' o 'procedimiento'. Facilita el proceso de la persona en inventario. Deben ser creados previamente y se necesita familarizacion con los 'servicios' o 'procedimientos'.

Attributes:

* `nombre = models.CharField(max_length=50, unique=True)`
* `descripcion = models.CharField(max_length=200)`
* `productos = models.ManyToManyField('inventario.Producto', through='PaqueteItem')`
* `is_inactive = models.BooleanField(default=False)`

### `CancelPaquete`

Inherits from `expedientedental.core.models.CancelledModel`.

El crear este modelo indica que el paquete en el `ForeignKey` esta desactivado. Se proporciona motivo y se agrega fecha de creacion.

Attributes:

* `paquete = models.ForeignKey(Paquete)`

### `PaqueteItem`

Productos de un paquete.

Attributes:

* `paquete = models.ForeignKey(Paquete)`
* `producto = models.ForeignKey('inventario.Producto')`
* `cantidad_producto = models.DecimalField(max_digits=8, decimal_places=2)`

### `PaqueteConsumido`

Indica un grupo de productos que saldran de inventario.

Attributes:

* `paquete = models.ForeignKey(Paquete, null=True)`
* `medico = models.ForeignKey(Medico)`
* `paciente = models.ForeignKey(Paciente)`
* `servicio = models.ForeignKey('servicios.Servicio', null=True)`
* `nota = models.TextField(blank=True)`
* `status = models.CharField()` - has choices.

Methods:

* `get_item_initials` - Asigna initials usando PaqueteItems con ForeignKey a Paquete.

* `precio_total` - Saca el total de todos los PaqueteConsumidoItems con ForeignKey a PaqueteConsumido.

### `CancelPaqueteConsumido`

Hereda del modelo abstracto CancelledModel (`expedientedental.core.CancelledModel`) que contiene 'motivo' y 'created_at'. Agrega relacion con la salida a cancelar.

### `PaqueteConsumidoItemManager`

Methods:

* `get_precio_total` - Suma el precio de PaqueteConsumidoItem.

### `PaqueteConsumidoItem`

Producto a salir de inventario. Contiene el precio de acorde al precio del producto y la cantidad que va de salida (se consume).

Attributes:

* `paquete_consumido = models.ForeignKey(PaqueteConsumido)`
* `producto = models.ForeignKey('inventario.Producto')`
* `cantidad = models.DecimalField(max_digits=8, decimal_places=2)`
* `precio = models.DecimalField(max_digits=8, decimal_places=2)`

Methods:

* `set_precio` - Calcula el precio correcto a asignar multiplicando el precio del producto por la cantidad de este.

### `ProductoConsumido`

Saca Productos de inventario sin necesidad de asociarse a un servicio y sin generar peticion (PaqueteConsumido).

**Nota:** No escribire los atributos ya que este modelo o funcionalidad no estan bien pensados. Necesita un buen analisis!

## Views

**expedientedental.consumidos.views**

### `Paquetes`

Lista de paquetes.

Inherits from:

* **django.views.generic.ListView**

### `PaqueteCreate`

Creates Paquete object with PaqueteItems. The magic is in the form!

Inherits from:

* **django.views.generic.CreateView**

### `PaqueteDetail`

Muestra detalle de paquete y da la opcion de marcar como 'surtido'.

Inherits from:

* **django.views.generic.UpdateView**

### `PaqueteCancel`

Inherits from:

* **expedientedental.core.CreateObjFromContext**

### `PaqueteCancelled`

Inherits from:

* **django.views.generic.ListView**

### `PaqueteCancelledDetail`

Inherits from:

* **django.views.generic.DetailView**



<!--
## Forms

**expedientedental.core.forms**

### `SimpleCrispyForm`

Inherits from:

* **django.forms.ModelForm**

#### Usage

Inherit from this form to get a simple crispified form with a submit button with the text 'Guardar'.

## Utils

**expedientedental.core.utils**

### `normalize_query(query_string)`

Requires:

* **re**

It receives a string as parameter and returns a list of 'terms'.

### `build_query(query_string, search_fields)`

Requires:

* **django.db.models.Q**

It normalizes the query string and does an icontains search for every term in every search field. It returns a query.

### `generic_search(request, model, fields, query_param='q')`

#### Usage

This is the function that gets called to perform a search. It gathers the parameters, the models and the fields. It runs those parameters with `build_query` and then returns search results.

```python
from core.utils import generic_search

from altas.models import Paciente

def paciente_search(request):
    query = 'q'
    model = Paciente.objects.all()
    fields = [
        'nombre',
        'apellidoMaterno',
        'apellidoPaterno',
        'CredencialPaciente'
    ]
    objects = generic_search(request, model, fields, query)

    return render(request, 'utilidad-search.html', {
        'objects': objects,
        'search_string': request.GET.get(query, '')
        })
```

You can also search multiple models:

```python
from core.utils import generic_search

from altas.models import Paciente

def person_search(request):
    query = 'q'
    model = Paciente.objects.all()
    MODEL_MAP = {
        Paciente: [
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'credencialPaciente',
        ]
        Medico: [
            'user',
            'mothers_last_name',
            'rfc',
        ]
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request, model, fields, query)

    return render(request, 'utilidad-search.html', {
        'objects': objects,
        'search_string': request.GET.get(query, '')
        })
```

### `paginate_objects`

Requires:

* **django.core.paginator.Paginator**
* **django.core.paginator.EmptyPage**

#### Usage

```python
# continued from the paciente_search above.
def paciente_search(request):
    [...]
    paginator, page_obj, object_list, is_paginated = paginate_objects(
        request, objects, 20)

    return render(request, 'utilidad-search.html', {
        'objects': object_list,
        'page_obj': page_obj,
        'paginator': paginator,
        'is_paginated': is_paginated,
        'search_string': request.GET.get(query, ''),
        'us_active': 'active'
        })
```

The function outputs four parameters, so you have to define all four. In this example, `paginator` represents the paginator itself which is a list, `page_obj` is the page method in the paginator which outputs an object, `object_list` is the queryset, and `is_paginated` returns a boolean from the `has_other_pages()` method.
 -->
