---
layout: page
title: Core
---

## Ir a

1. [Modelos](#modelos)
* [Vistas](#vistas)
* [Formas](#formas)
* [Utilidades](#utilidades)
* [Mixins](#mixins)


## Models

**expedientedental.core.models**

### `TimeStampedModel`

Modelo abstacto que agrega una marca de tiempo con la fecha de creaciony de modificacion del modelo.

Atributos:

* created_at - DateTimeField
* updated_at - DateTimeField

#### Uso

Hereda de este modelo cuando desees mantener control de la fecha de creacion y ultima modificacion.

```python
from core.models import TimeStampedModel

class PaqueteConsumido(TimeStampedModel):
    # [...]
```

### `CancelledModel`

Este otro modelo abstracto debera ser usado cuando un modelo tiene la opcion de ser cancelado.

Atributos:

* `created_at` - DateTimeField
* `reason` - TextField

#### Uso

Para desactivar un producto en inventario, se realizo lo siguiente:

```python
from core.models import CancelledModel

class CancelProducto(CancelledModel):
    producto = models.ForeignKey(Producto)
```

Puedes saber su un producto ha sido desactivado buscando un 'CancelledModel' de la siguiente manera:

```python
>>> from inventario.models import Producto, CancelProducto
>>> producto = Producto.objects.get(pk=1)
>>> producto_cancelado = CancelProducto.objects.get(producto=producto)
```

Para facilitar esto, un atributo se agrega al modelo que deseas cancelar o 'desactivar':

```python
class Producto(models.Model):
    # [...]
    is_active = models.BooleanField(default=True)
```

## Vistas

**expedientedental.core.views**

### `CreateObjFromContext`

Hereda de:

* **django.views.generic.CreateView**

Atributos:

* `ctx_model`
* `initial_value`

Metodos:

* `get_obj`
* `get_context_data` - agrega al metodo heredado.
* `get_initial` - agrega al metodo heredado.

#### Uso

Debes heredar de esta vista cuando desees crear un objeto al hacer referencia a un segundo objeto desde el url.

```python
from core.views import CreateObjFromContext

class RadiografiaCreate(CreateObjFromContext):
    ctx_model = Paciente  # el modelo que viene del url
    initial_value = 'paciente'  # como se llama el objeto en el objeto que esta siendo creado
    form_class = RadiografiaForm
    template_name = 'radiografia.html'
```

**Nota:** Si no estas segura en que es `initial_value`, consulta la forma de la vista y el modelo del objeto que esta siendo creado.

### `DetailListView`

Da la posibilidad de llamar una lista de objetos con paginacion en una vista de detalle. La mayor parte del codigo fue tomada de **django.views.generic.list.MultipleObjectMixin**.

Hereda de:

* **django.views.generic.DetailView**

Atributos:

* `list_model`
* `list_queryset`
* `list_paginate_by`
* `list_context_name`

Metodos:

* `get_list_queryset` - objetos a ser manipulados o un queryset de los objetos.
* `get_list_paginate_by(queryset)` - obtiene el numero de objetos por el cual paginar la lista.
* `paginate_queryset(queryset, page_size)` - pagina el queryset, si es necesario.
* `get_list_context_object_name(object_list)` - obtiene el nombre de la lista de objetos a ser usados en el contexto.
* `get_context_data(**kwargs)` - agrega al metodo heredado e integra paginacion y variables del queryset.

#### Uso

Si te das cuenta que tienes una vista de detalle y una lista de objetos en el contexto, seria mejor heredar de esta vista. La paginacion es opcional.

```python
from core.views import DetailListView

class ServiciosPaciente(DetailListView):
    model = Paciente  # the main model, or the one that comes from the context.
    context_object_name = 'paciente'
    list_model = Servicio  # the model you wish to have in a list.
    list_queryset = list_model.objects.filter(status__in=['parcial', 'pagado'])
    list_paginate_by = 20  # you wish to paginate the objects every 20.
    list_context_name = 'servicios'  # what you want it to be called in the template.
    template_name = 'utilidad-servicios.html'
```

## Formas

**expedientedental.core.forms**

### `SimpleCrispyForm`

Hereda de:

* **django.forms.ModelForm**

#### Uso

Hereda de esta forma para obtener una forma simple y crispificada con un boton de submit y el texto 'Guardar'.

## Utilidades

**expedientedental.core.utils**

### `normalize_query(query_string)`

Requiere:

* **re**

Recive una cadena como parametro y retorna una lista de terminos.

### `build_query(query_string, search_fields)`

Requiere:

* **django.db.models.Q**

Normaliza la cadena de la consulta y hace una busqueda tipo `icontains` por cada termino en cada campo de busqueda. Retorna una consulta.

### `generic_search(request, model, fields, query_param='q')`

#### Uso

Esta es la funcion que se llama para llevar a cabo una busqueda. Obtiene los parametros, los modelos y los campos. Corre esos parametros con `build_query` y retorna los resultados de la busqueda.

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

Tambien puedes buscar multiples modelos:

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

Requiere:

* **django.core.paginator.Paginator**
* **django.core.paginator.EmptyPage**

#### Uso

```python
# continuado del ejemplo de paciente_search arriba.
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

La funcion retorna cuatro parametros, entonces debes definir los cuatro. En este ejemplo, `paginator` representa el paginador en si el cual es una lista, `page_ogj` es el metodo de `page` en el paginador y retorna un objeto, `object_list` es el queryset e `is_paginated` retorna un booleano del metodo `has_other_pages().

## Mixins

Para leer sobre los mixins en core, busca la documentacion de 'django-braces'.
