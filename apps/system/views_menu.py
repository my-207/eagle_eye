from django.views.generic import ListView
from django.shortcuts import HttpResponse, get_object_or_404
import json
from .mixin import LoginRequiredMixin
from apps.custom import SandboxCreateView, SandboxUpdateView, BreadcrumbMixin
from .models import Menu
from django.views.generic.base import View


class MenuCreateView(SandboxCreateView):
    model = Menu
    fields = '__all__'

    def get_context_data(self, **kwargs):
        kwargs['menu_all'] = Menu.objects.all()
        return super().get_context_data(**kwargs)


class MenuListView(LoginRequiredMixin, BreadcrumbMixin, ListView):
    model = Menu
    context_object_name = 'menu_all'


class MenuUpdateView(SandboxUpdateView):
    model = Menu
    fields = '__all__'
    template_name_suffix = '_update'

    def get_context_data(self, **kwargs):
        kwargs['menu_all'] = Menu.objects.all()
        return super().get_context_data(**kwargs)


class MenuDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST['id'].split(','))
            try:
                 if Menu.objects.filter(parent_id=request.POST['id']):
                    ret['result'] = False
                 else:
                     Menu.objects.filter(id__in=id_list).delete()
                     ret['result'] = True
            except Menu.DoesNotExist:
                raise Menu.objects.filter(id__in=id_list)
        return HttpResponse(json.dumps(ret), content_type='application/json')

#ceshi
