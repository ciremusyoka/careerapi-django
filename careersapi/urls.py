"""template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Careers API Documentation.",
#       default_version='v1',
#       description="API Documentation",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="michameiu@gmail.com"),
#       license=openapi.License(name="Private software"),
#    ),
#    validators=['flex', 'ssv'],
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )


urlpatternsv1=[
    # url(r'^clients/',include('client.urlsV1')),
    # url(r'^games/',include('game.urlsV1')),
    url(r'^users/',include('client.urlsv1')),
    url(r'^schools/',include('school.urlsv1')),
    url(r'^subjects/',include('school.subject.urlsv1')),
    url(r'^subject-results/',include('school.subject_result.urlsv1')),
    url(r'^results/',include('school.result.urlsv1')),
    url(r'^universities/',include('university.urlsv1')),
    url(r'^professions/',include('university.profession.urlsv1')),
    url(r'^courses/',include('university.course.urlsv1')),
    url(r'^course-cutoffs/',include('university.course_cutoff.urlsv1')),
    url(r'^personalities/', include('prediction.personality.urlsv1')),
    url(r'^predictions/', include('prediction.urlsv1')),

]

urlpatternsv2=[
    # url(r'^clients/',include('client.urlsV1')),
    # url(r'^games/',include('game.urlsV1')),
    # url(r'^users/',include('client.urlsv1')),
]




#versions from the Apis(v1,v2)
apiversionsurlsparterns=[
    url(r'^v1/',include(urlpatternsv1)),
    url(r'^v2/',include(urlpatternsv2))
]



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('drf_autodocs.urls')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^api/', include(apiversionsurlsparterns)),
    # url(r'^predictions/', include('prediction.urlsv1')),

]

