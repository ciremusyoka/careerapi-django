from django.db import models
from rest_framework.exceptions import APIException
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission
from django_filters.rest_framework import FilterSet

class MyAbstractModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


COUNTIES=(('NAI','Nairobi'),('KIS','Kisumu'))


def get_dynamic_model_filter_class(model_class):
    # for s in survey.formulas.all().values_list("slug",flat=True):
    #     slugs.append(s)
    # myextra_kwargs = {f.name: {"required": True} for f in model_class._meta.fields if not f.blank}
    class Meta:
        model = model_class
        fields = ("__all__")
        exclude=("image","logo","file")
        # extra_kwargs = myextra_kwargs

    attrs = {"Meta": Meta}
    serializer = type('Response' + model_class.__class__.__name__ + "Filter", (FilterSet,), attrs)
    return serializer

class MyStandardPagination(PageNumberPagination):
    page_size = 100
    max_page_size = 1000
    page_size_query_param = 'page_size'

class MyCustomException(APIException):
    status_code = 503
    detail = "Service temporarily unavailable, try again later."
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

    def __init__(self, message, code=400):
        self.status_code = code
        self.default_detail = message
        self.detail = message


class IsAuthenticatedOrOptions(BasePermission):
    safe_methods = ["OPTIONS", ]

    def has_permission(self, request, view):
        if request.method in self.safe_methods:
            return True
        return request.user.is_authenticated()
