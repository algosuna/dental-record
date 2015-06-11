from django.views.generic import CreateView


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
