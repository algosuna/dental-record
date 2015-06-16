from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
from django.core.exceptions import ImproperlyConfigured
from django.utils.encoding import smart_str
from django.views.generic import CreateView, DetailView


class CreateObjFromContext(CreateView):
    '''
    Base class that contains methods used when creating an object with data
     from the url.
    '''
    ctx_model = None
    initial_value = None

    def get_obj(self):
        obj = self.ctx_model.objects.get(pk=self.kwargs.get('pk'))
        return obj

    def get_context_data(self, **kwargs):
        ctx = super(CreateObjFromContext, self).get_context_data(**kwargs)
        ctx.update({self.initial_value: self.get_obj()})
        return ctx

    def get_initial(self):
        initial = super(CreateObjFromContext, self).get_initial()
        initial = initial.copy()
        initial[self.initial_value] = self.get_obj()
        return initial

    # TODO: add a method for the success url.


class DetailListView(DetailView):
    '''
    Enables a detail view to call some objects with pagination.
    Most from django.views.generic.list.MultipleObjectMixin.
    '''
    list_model = None
    list_queryset = None
    list_paginate_by = None
    list_context_name = None

    def get_list_queryset(self):
        '''
        Objects to be manipulated, if a queryset is defined, then it uses that.
        '''
        if self.list_queryset is not None:
            queryset = self.list_queryset
        elif self.list_model is not None:
            queryset = self.list_model._default_manager.all()
        else:
            raise ImproperlyConfigured(
                "'%s' must define 'list_queryset' or 'list_model'"
                % self.__class__.__name__)
        return queryset

    def get_list_paginate_by(self, queryset):
        return self.list_paginate_by

    def paginate_queryset(self, queryset, page_size):
        ''' Paginate the queryset, if needed. '''
        paginator = Paginator(queryset, page_size)
        page = self.kwargs.get('page') or self.request.GET.get('page') or 1
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404(
                    "Page is not 'last', nor can it be converted to an int.")
        try:
            page = paginator.page(page_number)
            return (paginator, page, page.object_list, page.has_other_pages())
        except InvalidPage:
            raise Http404('Invalid page (%(page_number)s)' % {
                          'page_number': page_number
                          })

    def get_list_context_object_name(self, object_list):
        ''' Get the name of the item to be used in the context. '''
        if self.list_context_name:
            return self.list_context_name
        elif hasattr(object_list, 'model'):
            return smart_str(
                '%s_list' % object_list.model._meta.object_name.lower())
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super(DetailListView, self).get_context_data(**kwargs)
        queryset = self.get_list_queryset()
        page_size = self.get_list_paginate_by(queryset)
        list_context_name = self.get_list_context_object_name(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(
                queryset, page_size)
            context.update({
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset
            })
        else:
            context.update({
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset
            })
        context.update(kwargs)
        if list_context_name is not None:
            context[list_context_name] = queryset
        return context
