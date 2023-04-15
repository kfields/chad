from chad.schema.schemata import Connection, Edge, Node


class AgentNode(Node):
    def __init__(self, objekt):
        super().__init__(objekt)

class AgentEdge(Edge):
    def __init__(self, obj, node_class=AgentNode):
        super().__init__(obj, node_class)

class AgentConnection(Connection):
    def __init__(self, objs):
        super().__init__(objs, edge_class=AgentEdge, node_class=AgentNode)
