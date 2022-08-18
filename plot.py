import pydot
import numpy as np
from cannibal import Node,game
import os
os.environ["PATH"] += os.pathsep + 'F:/Ankit study/7th Sem/AI/Assignment-1/Graphviz/bin'
 
class draw:
    def __init__(self):
        self.graph = pydot.Dot('my_graph', graph_type='digraph', bgcolor='white')

    def draw_self(self,given_node:Node):
        if given_node.parent==None:
            root_node=pydot.Node('root', label=str(given_node.current_state))
            root_node.add_style('filled')
            root_node.set_fillcolor(given_node.color)
            self.graph.add_node(root_node)
        else:
            new_node=pydot.Node(str(given_node.current_state)+str(given_node.parent.current_state), label=str(given_node.current_state))
            new_node.add_style('filled')
            new_node.set_fillcolor(given_node.color)
            self.graph.add_node(new_node)

    def connect(self,given_node:Node):
        if given_node.parent==None:
            return
        if given_node.parent.parent!=None:
            difference=np.subtract([3,3,0],given_node.current_state)
            self.graph.add_edge(pydot.Edge(str(given_node.parent.current_state)+str(given_node.parent.parent.current_state),str(given_node.current_state)+str(given_node.parent.current_state),label=str(difference)))
        elif given_node.parent.parent==None and given_node.parent!=None:
            difference=np.subtract([3,3,0],given_node.current_state)
            self.graph.add_edge(pydot.Edge('root',str(given_node.current_state)+str(given_node.parent.current_state),label=str(difference)))

    def generate_state_space(self):
        self.graph.write_png('try.png')

if __name__=='__main__':
    initial=Node([3,3,0])
    new_game=game(initial)
    all_nodes=new_game.generate_nodes_bfs(initial)
    print(len(all_nodes))
    drawing=draw()
    for node in all_nodes:
        drawing.draw_self(node)
        drawing.connect(node)
    drawing.generate_state_space()