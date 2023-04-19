from graphql.pyutils import SimplePubSub

from ariadne import QueryType, MutationType, SubscriptionType, InterfaceType
from ariadne_relay import NodeObjectType, RelayQueryType, resolve_node_query

from ...subscription import SubscriptionAwareObjectType

#query = QueryType()
# Instead of using Ariadne's QueryType, use the Relay-enabled
# RelayQueryType class
query = RelayQueryType()

# resolve_node_query is provided as a resolver for Query.node()
query.set_field("node", resolve_node_query)

mutation = MutationType()
#subscription = SubscriptionType()
subscription = SubscriptionAwareObjectType("Subscription")
pubsub = SimplePubSub()

# Define the Node interface
node = InterfaceType("Node")

# Add a Node type resolver
@node.type_resolver
def resolve_node_type(obj, *_):
    return obj.__class__.__name__