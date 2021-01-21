#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 13:24:07 2020

@author: graceshi

Instructions: Just click run! The code will run 10 iterations (changeable in the main) and generate the graph, and return
True for cop win and False for robber win. 
"""


import random
import networkx as nx 
import matplotlib.pyplot as plt 

class Environment:
    def __init__(self, cops, robbers , graph):
        self.cop = cops # cop number
        self.robber = robbers # robber number
        self.graph = graph # nx.Graph object
        
        
    # marking algorithm to determine if cop can win game
    def marking(self):
        unmarked_states = set()
        for u in self.graph:
            for v in self.graph:
                unmarked_states.add((u,v))
                
        
        marked_states = set()
        
        
        for u in self.graph:
            unmarked_states.remove((u,u))
            marked_states.add((u,u))
    
        repeat = True
        while unmarked_states and repeat:
            repeat = False
            for c in self.graph:
                for r in self.graph:
                    if c != r and (c,r) not in marked_states:
                        for r_p in self.graph.neighbors(r):
                            for c_p in self.graph.neighbors(c):
                                if (c_p, r_p) in marked_states:
                                    try:
                                        unmarked_states.remove((c,r))
                                    except:
                                        pass
                                    marked_states.add((c,r))
                                    repeat = True
                                    break
                 
        
        if unmarked_states:
            print(unmarked_states)
            return False
        
        return True

    # displays graph and initial cop robber positions
    def display(self):
        color_map = []
        for node in self.graph:
            color_map.append('grey')   
#            if node == self.cop and node == self.robber:
#                color_map.append('green')
#            elif node == self.cop:
#                color_map.append('blue')
#            elif node == self.robber:
#                color_map.append('red')
#            else: 
#                color_map.append('grey')      
        nx.draw(self.graph, node_color=color_map, with_labels=True)
        plt.show()
        
    
    

def generate_graph(node_count, edge_count):

    g = nx.MultiDiGraph() # direced graph 
    
    for i in range(edge_count):
         x = random.randint (1, node_count)
         y = random.randint (1, node_count)
         if x == y: continue
         
         g.add_edge(x,y)

    return g

if __name__ == "__main__":
    
    edges = []
    results = []
    for k in range(1, 100):
        edges.append(k)
        graph = generate_graph(10, k)
        env = Environment(1, 1, graph)
            
        env.display()
        results.append(env.marking())

    plt.scatter(edges, results)
    plt.xlabel("Number of Edges")
    plt.ylabel("Results")