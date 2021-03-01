from pydot import Dot, Node, Edge

# Create graph
roadmap = Dot("roadmap")

# Create nodes
roadmap.add_node(Node(name="expressions", label="Expressions"))
roadmap.add_node(Node(name="variables", label="Variables"))

# Create edges
roadmap.add_edge(Edge(src="expressions", dst="variables", style="dotted"))

# Export svg
roadmap.write_svg("roadmap.svg")
