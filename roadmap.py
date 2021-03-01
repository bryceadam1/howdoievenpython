from pydot import Dot, Node, Edge

# Create graph
roadmap = Dot("roadmap")

# Create nodes
roadmap.add_node(Node(name="expressions", label="Expressions"))
roadmap.add_node(Node(name="variables", label="Variables"))
roadmap.add_node(Node(name="types", label="Types"))
roadmap.add_node(Node(name="lists-and-objects", label="Lists and Objects"))
roadmap.add_node(Node(name="conditional-statements-logic", label="Conditional Statements and Logic"))
roadmap.add_node(Node(name="functions", label="Functions"))
roadmap.add_node(Node(name="loops-list-comprehensions", label="Loops and List Comprehensions"))
roadmap.add_node(Node(name="recursion", label="Recursion"))
roadmap.add_node(Node(name="packages-and-numpy", label="Packages and Numpy"))
roadmap.add_node(Node(name="plotting-with-matplotlib", label="Plotting with Matplotlib"))
roadmap.add_node(Node(name="linear-algebra-numpy", label="Linear Algebra with Numpy"))
roadmap.add_node(Node(name="advanced-topics-roundoff", label="Advanced Topics: Roundoff Error"))
roadmap.add_node(Node(name="advanced-topics-complexity", label="Advanced Topics: Algorithmic Complexity"))

roadmap.add_node(Node(name="common-errors", label="Common Errors"))
roadmap.add_node(Node(name="helpful-functions", label="Helpful Functions"))

# Create edges
roadmap.add_edge(Edge(src="expressions", dst="variables"))
roadmap.add_edge(Edge(src="variables", dst="types"))
roadmap.add_edge(Edge(src="types", dst="lists-and-objects"))
roadmap.add_edge(Edge(src="types", dst="conditional-statements-logic"))
roadmap.add_edge(Edge(src="conditional-statements-logic", dst="functions"))
roadmap.add_edge(Edge(src="lists-and-objects", dst="loops-list-comprehensions"))
roadmap.add_edge(Edge(src="functions", dst="recursion"))
roadmap.add_edge(Edge(src="loops-list-comprehensions", dst="recursion"))
roadmap.add_edge(Edge(src="functions", dst="packages-and-numpy"))
roadmap.add_edge(Edge(src="packages-and-numpy", dst="plotting-with-matplotlib"))
roadmap.add_edge(Edge(src="packages-and-numpy", dst="linear-algebra-numpy"))
roadmap.add_edge(Edge(src="loops-list-comprehensions", dst="linear-algebra-numpy"))
roadmap.add_edge(Edge(src="linear-algebra-numpy", dst="advanced-topics-roundoff"))
roadmap.add_edge(Edge(src="recursion", dst="advanced-topics-complexity"))
roadmap.add_edge(Edge(src="linear-algebra-numpy", dst="advanced-topics-complexity"))

# Export svg
roadmap.write_svg("roadmap.svg")
