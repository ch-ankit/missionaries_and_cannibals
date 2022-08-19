import pydot
import numpy as np
from cannibal import Node,game
import os
os.environ["PATH"] += os.pathsep + 'F:/Ankit study/7th Sem/AI/Assignment-1/Graphviz/bin'
 
class draw:
    def __init__(self):
        self.graph = pydot.Dot('my_graph', graph_type='digraph', bgcolor='skyblue')

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
            if given_node.current_state[2]==1:
                difference=np.absolute(given_node.current_state-given_node.parent.current_state)[:2]
            else:
                difference=np.absolute(given_node.parent.current_state-given_node.current_state)[:2]
            self.graph.add_edge(pydot.Edge(str(given_node.parent.current_state)+str(given_node.parent.parent.current_state),str(given_node.current_state)+str(given_node.parent.current_state),label=str(difference)))
        elif given_node.parent.parent==None and given_node.parent!=None:
            if given_node.current_state[2]==1:
                difference=np.absolute(given_node.current_state-given_node.parent.current_state)[:2]
            else:
                difference=np.absolute(given_node.parent.current_state-given_node.current_state,)[:2]
            self.graph.add_edge(pydot.Edge('root',str(given_node.current_state)+str(given_node.parent.current_state),label=str(difference)))

    def generate_state_space(self):
        self.legend()
        self.graph.write_png('try.png')

    def legend(self):
        graphlegend = pydot.Cluster(graph_name="legend", label="Legend", fontsize="20", color="red",
                                    fontcolor="blue", style="filled", fillcolor="white")
        processed_node = pydot.Node('Processed node', shape="plaintext")
        graphlegend.add_node(processed_node)
        dead_node = pydot.Node("Dead Node", shape="plaintext")
        graphlegend.add_node(dead_node)
        already_generated = pydot.Node('Already Generated', shape="plaintext")
        graphlegend.add_node(already_generated)
        goal_node = pydot.Node('Goal Node', shape="plaintext")
        graphlegend.add_node(goal_node)
        note1=pydot.Node('Node [x,y,z]=> x,y = No. of missionaries and cannibals at left shore\n'
                           'If z=1 -> boat at right shore\n'
                           'If z=0-> boat at left shore\n'
                           , shape="plaintext",fontsize="18")
        note2=pydot.Node('Edge [x,y]=> Move x missionaries and y cannibals\n'
                            'Move x missionaries and y cannibals'
                           , shape="plaintext",fontsize="18")
        green_node = pydot.Node("1", style="filled", fillcolor="seagreen1", label="")
        graphlegend.add_node(green_node)
        red_node = pydot.Node("2", style="filled", fillcolor="lightsalmon", label="")
        graphlegend.add_node(red_node)
        yellow_node = pydot.Node("3", style="filled", fillcolor="yellow", label="")
        graphlegend.add_node(yellow_node)
        blue_node = pydot.Node("4", style="filled", fillcolor="cornflowerblue", label="")
        graphlegend.add_node(blue_node)
        graphlegend.add_node(note1)
        graphlegend.add_node(note2)


        self.graph.add_subgraph(graphlegend)
        self.graph.add_edge(pydot.Edge(green_node, processed_node, style="invis"))
        self.graph.add_edge(pydot.Edge(red_node, dead_node, style="invis"))
        self.graph.add_edge(pydot.Edge(processed_node, yellow_node, style="invis"))
        self.graph.add_edge(pydot.Edge(yellow_node, already_generated, style="invis"))
        self.graph.add_edge(pydot.Edge(dead_node, blue_node, style="invis"))
        self.graph.add_edge(pydot.Edge(blue_node, goal_node, style="invis"))
        self.graph.add_edge(pydot.Edge(goal_node, note1, style="invis"))
        self.graph.add_edge(pydot.Edge(already_generated, note2, style="invis"))

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