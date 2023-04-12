from chad.schema.schemata import Connection, Edge, Node


class ChatNode(Node):
    def __init__(self, objekt):
        super().__init__(objekt)

class ChatEdge(Edge):
    def __init__(self, obj, node_class=ChatNode):
        super().__init__(obj, node_class)

class ChatConnection(Connection):
    def __init__(self, objs):
        super().__init__(objs, edge_class=ChatEdge, node_class=ChatNode)
