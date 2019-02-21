from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView

from mylib.my_common import MyStandardPagination, MyCustomException, get_dynamic_model_filter_class
from mylib.mymixins import MyCreateModelMixin, MyListModelMixin


class MyListCreateAPIView(MyCreateModelMixin,MyListModelMixin,
                    GenericAPIView):
    """
    Concrete view for creating a model instance.

    """
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MyDjangoFilterBackend(DjangoFilterBackend):
    myfilter_class = None

    def get_filter_class(self, view, queryset=None):
        """
        Return the django-filters `FilterSet` used to filter the queryset.
        """

        if self.myfilter_class:
            return self.myfilter_class
        query = getattr(view, 'queryset', None)
        try:
            model = query.model
            filter_model = model
            filter_class = get_dynamic_model_filter_class(model)
            assert issubclass(queryset.model, filter_model), \
                'FilterSet model %s does not match queryset model %s' % \
                (filter_model, queryset.model)
            self.myfilter_class = filter_class
            return filter_class
        except Exception as e:
            print(e)
            raise MyCustomException("The View must inherit from MyDynamicGetSerializerQuerysetModelMixin ")

    def filter_queryset(self, request, queryset, view):
        filter_class = self.get_filter_class(view, queryset)
        if filter_class:
            return filter_class(request.query_params, queryset=queryset).qs
        return queryset
