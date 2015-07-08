---
layout: page
title: Core
---

## Jump to

1. [Models](#models)
* [Views](#views)
* [Forms](#forms)
* [Utils](#utils)
* [Mixins](#mixins)


## Models

**expedientedental.core.models**

### `TimeStampedModel`
Abstract model that adds a timestamp to the created date and the modified date of the model.

Attributes:

* created_at - DateTimeField
* updated_at - DateTimeField

#### Usage

Inherit from this model whenever you want to keep control of creation date and latest modification.

```python
from core.models import TimeStampedModel

class PaqueteConsumido(TimeStampedModel):
    # [...]
```

### `CancelledModel`

This other abstract model should be used when a model has the option of getting cancelled.

Attributes:

* `created_at` - DateTimeField
* `reason` - TextField

#### Usage

To deactivate a product in inventory, the following was done:

```python
from core.models import CancelledModel

class CancelProducto(CancelledModel):
    producto = models.ForeignKey(Producto)
```

You can tell a product was deactivated by looking for a CancelledModel like this:

```python
>>> from inventario.models import Producto, CancelProducto
>>> producto = Producto.objects.get(pk=1)
>>> producto_cancelado = CancelProducto.objects.get(producto=producto)
```

To make this easier, an attribute is added to the model you wish to cancel or 'deactivate':

```python
class Producto(models.Model):
    # [...]
    is_active = models.BooleanField(default=True)
```

## Views

**expedientedental.core.views**

### `CreateObjFromContext`

Inherits from:

* **django.views.generic.CreateView**

Attributes:

* `ctx_model`
* `initial_value`

Methods:

* `get_obj`
* `get_context_data` - adds to inherited method.
* `get_initial` - adds to inherited method.

#### Usage

You should inherit from this view when you wish to create an object while referencing a second object from the url.

```python
from core.views import CreateObjFromContext

class RadiografiaCreate(CreateObjFromContext):
    ctx_model = Paciente  # the model that comes from the url
    initial_value = 'paciente'  # what the value is called in the object being created.
    form_class = RadiografiaForm
    template_name = 'radiografia.html'
```

**Note:** If you are still not clear on what `initial_value` is, look at the view's form and the model of the object being created.

### `DetailListView`

Enables a detail view to call some objects with pagination. Most of the code was taken from **django.views.generic.list.MultipleObjectMixin**.

Inherits from:

* **django.views.generic.DetailView**

Attributes:

* `list_model`
* `list_queryset`
* `list_paginate_by`
* `list_context_name`

Methods:

* `get_list_queryset` - objects to be manipulated or a queryset of the objects.
* `get_list_paginate_by(queryset)` - gets the number of objects the list should be paginated by.
* `paginate_queryset(queryset, page_size)` - paginate the queryset, if needed.
* `get_list_context_object_name(object_list)` - get the name of the list objects to be used in the context.
* `get_context_data(**kwargs)` - adds to inherited method and integrates pagination and queryset variables.

#### Usage

If you find yourself with a detail view with a list of objects, you should inherit from this view. The pagination is optional.

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

# TODO: explain the multiple model search and fix the above code to match this.

### `paginate_objects`

Requires:

* **django.core.paginator.Paginator**
* **django.core.paginator.EmptyPage**


# TODO: add sample usage
