from django.conf.urls import url

from prediction.views import ListCreatePredictions, RetrieveUpdateDestroyPredictions

urlpatterns= [
    url(r'^$', ListCreatePredictions.as_view(), name="list_create_predictions"),
    url(r'^(?P<pk>[0-9]+)/?$', RetrieveUpdateDestroyPredictions.as_view(), name="retrieve_update_destroy_prediction"),
]