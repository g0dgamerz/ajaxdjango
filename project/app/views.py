from django.shortcuts import render
from .forms import AjaxForm
from django.views.generic import FormView
from django.http import JsonResponse
from .mixins import AjaxFormMixin
from .forms import AjaxForm

# Create your views here.
class AjaxFormView(AjaxFormMixin, FormView):
    form_class = AjaxForm
    template_name  = 'forms/ajax.html'
    success_url = '/form-success/'

    def form_invalid(self, form):
        response = super(JoinFormView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxFormView, self).form_valid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return response