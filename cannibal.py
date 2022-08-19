import numpy as np

class Bank:
    def __init__(self, missionaries, cannibals):
        self.missionaries=missionaries
        self.cannibals=cannibals

    def is_valid(self):
        if self.missionaries!=0:
            if self.missionaries>=self.cannibals:
                return True
            else:
                return False
        return True

class Node:
    def __init__(self,curr_state,generated=False, children= np.empty((0,1)), parent=None, color='seagreen1'):
        self.current_state=np.array(curr_state,dtype=int)

        self.left_bank_state=Bank(3-curr_state[0],3-curr_state[1])
        self.right_bank_state=Bank(curr_state[0],curr_state[1])

        
        self.generated=generated
        self.children=children
        self.parent=parent
        self.color=color

        self.edges=np.array([
            [1,0],[1,1],[0,2],[0,1],[2,0]
        ])

    def valid_edges(self):
        edges=np.empty(shape=(0,2), dtype=int)
        if self.current_state[2]==1:
            for x in self.edges:
                if self.left_bank_state.missionaries-x[0]>=0 and self.left_bank_state.cannibals-x[1]>=0:
                    edges=np.append(edges,[x],axis=0)
        else:
            for x in self.edges:
                if self.right_bank_state.missionaries-x[0]>=0 and self.right_bank_state.cannibals-x[1]>=0:
                    edges=np.append(edges,[x],axis=0)
        return edges
            
    def is_feasible(self):
        if self.left_bank_state.is_valid() and self.right_bank_state.is_valid():
            return True
        else:
            self.color='lightsalmon'
            return False
        
    def generate_children(self):
        if not self.generated and self.is_feasible():
            if self.current_state[2]==1:
                for x in self.valid_edges():
                    self.children=np.append(self.children,np.array([Node([self.right_bank_state.missionaries+x[0],self.right_bank_state.cannibals+x[1], 0],parent=self)]))
            else:
                for x in self.valid_edges():
                    self.children=np.append(self.children,np.array([Node([self.right_bank_state.missionaries-x[0],self.right_bank_state.cannibals-x[1], 1], parent=self)]))
        return self.children

class game:
    def __init__(self, initial_node:Node, generated_states=np.empty((0,3),dtype=int)):
        if initial_node.is_feasible():
            self.initial_node=initial_node
        else:
            print('Given state is invalid')
        self.generated_states=generated_states
        self.nodes=np.empty((0,1))
        self.nodes=np.append(self.nodes,self.initial_node)

    def generate_nodes_bfs(self,given_node:Node):
        comparision_list=self.generated_states.tolist()
        if (given_node.current_state.tolist() not in comparision_list) and [0,0,1] not in comparision_list:
            if given_node.current_state.tolist() != [0,0,1]:
                self.nodes=np.append(self.nodes,given_node.generate_children())
            given_node.generated=True
            for generated_nodes in self.nodes:
                generated_nodes.is_feasible()
                if [0,0,1] in self.generated_states.tolist():
                    break
                self.generated_states=np.append(self.generated_states,[given_node.current_state],axis=0)
                if not generated_nodes.generated and generated_nodes.color=='seagreen1':
                    self.generate_nodes_bfs(generated_nodes)
        else:
            return 
        self.final_color_code()
        return self.nodes
    def final_color_code(self):
        for node in self.nodes:
            if not node.generated and node.color=='seagreen1':
                node.color='yellow'
            if node.current_state.tolist()==[0,0,1]:
                node.color='cornflowerblue'
if __name__=="__main__":
    initial=Node([3,3,0])
    new_game=game(initial)
    all_nodes=new_game.generate_nodes_bfs(initial)
    print(len(all_nodes))
    for node in range(1,len(all_nodes)):
        print(all_nodes[node].current_state,all_nodes[node].color,all_nodes[node].generated, all_nodes[node].parent.current_state)
