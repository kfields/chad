from ariadne import QueryType, ObjectType, make_executable_schema
from ariadne_django.scalars import date_scalar, datetime_scalar
from ariadne_django.type_defs import DjangoObjectType
from ariadne_django.views import GraphQLView
from django.contrib.auth import get_user_model
from django.db.models import Q
from django_filters import FilterSet, OrderingFilter
from graphene import Node
from graphql_relay.connection.arrayconnection import offset_to_cursor, cursor_to_offset

class UserNode(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'email',
            'date_joined',
            'last_login',
            'first_name',
            'last_name',
        )
        interfaces = (Node,)

    @classmethod
    def get_node(cls, info, id):
        return get_user_model().objects.get(pk=id)

class UserFilter(FilterSet):
    class Meta:
        model = get_user_model()
        fields = {
            'username': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            'date_joined': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'last_login': ['exact', 'gt', 'lt', 'gte', 'lte'],
        }

class UserOrderingFilter(OrderingFilter):
    class Meta:
        model = get_user_model()
        fields = {
            'id': ['exact'],
            'username': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'date_joined': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'last_login': ['exact', 'gt', 'lt', 'gte', 'lte'],
        }

def resolve_users(info, **kwargs):
    queryset = get_user_model().objects.all()

    # Apply filters
    filterset = UserFilter(kwargs, queryset=queryset)
    queryset = filterset.qs

    # Apply sorting
    ordering_filter = UserOrderingFilter(kwargs, queryset=queryset, fields=UserOrderingFilter.Meta.fields)
    queryset = ordering_filter.qs

    # Paginate
    first = kwargs.get('first')
    last = kwargs.get
