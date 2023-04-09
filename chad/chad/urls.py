from django.contrib import admin
from django.urls import path

from ariadne_django.views import GraphQLView

from chad.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),
]
