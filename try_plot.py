import pydot
import os
os.environ["PATH"] += os.pathsep + 'F:/Ankit study/7th Sem/AI/Assignment-1/Graphviz/bin'

graph = pydot.Dot('my_graph', graph_type='graph', bgcolor='white')

a=[[3,3,0],[2,3,1]]

for node in a:
    my_node=pydot.Node(str(node),label=str(node))
    my_node.add_style('filled')
    my_node.set_fillcolor('green')
    graph.add_node(my_node)
    # graph.add_edge(pydot.Edge())
# Add nodes
# my_node = pydot.Node('a', label='Foo')
# graph.add_node(my_node)
# # Or, without using an intermediate variable:
# graph.add_node(pydot.Node('b', shape='circle'))

# # Add edges
# my_edge = pydot.Edge('a', 'b', color='blue')
# graph.add_edge(my_edge)
# # Or, without using an intermediate variable:
# graph.add_edge(pydot.Edge('b', 'c', color='blue'))

graph.write_png('output.png')
