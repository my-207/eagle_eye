from django.views.generic import TemplateView

from apps.system.mixin import LoginRequiredMixin
from custom import BreadcrumbMixin


class BusinessView(LoginRequiredMixin, BreadcrumbMixin, TemplateView):

    template_name = 'test/test.html'


class BusinessText(LoginRequiredMixin, BreadcrumbMixin, TemplateView):

    template_name = 'test/test.html'


class BusinessTextSearch(LoginRequiredMixin, BreadcrumbMixin, TemplateView):

    template_name = 'test/test-search.html'