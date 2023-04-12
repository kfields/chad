from django.contrib import admin
from django.urls import path
from django.conf import settings

#from ariadne_django.views import GraphQLView
from ariadne_django.views import GraphQLAsyncView

from chad.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),
    path('graphql/', GraphQLAsyncView.as_view(schema=schema), name='graphql'),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
