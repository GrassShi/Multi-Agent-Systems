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
        
        
        
    # baseline 
#    # marking algorithm to determine if cop can win game
#    def marking(self):
#        unmarked_states = set()
#        for u in self.graph:
#            for v in self.graph:
#                unmarked_states.add((u,v))
#                
#        
#        marked_states = set()
#        
#        
#        for u in self.graph:
#            unmarked_states.remove((u,u))
#            marked_states.add((u,u))
#    
#        repeat = True
#        while unmarked_states and repeat:
#            repeat = False
#            for c in self.graph:
#                for r in self.graph:
#                    if c != r and (c,r) not in marked_states:
#                        for r_p in [n for n in self.graph[r]]:
#                            for c_p in [n for n in self.graph[c]]:
#                                if (c_p, r_p) in marked_states:
#                                    try:
#                                        unmarked_states.remove((c,r))
#                                    except:
#                                        pass
#                                    marked_states.add((c,r))
#                                    repeat = True
#                                    break
#                 
#        
#        if unmarked_states:
#            return False
#        
#        return True
    
    
    # extension 1
    # marking algorithm to determine if cop can win game
    def marking(self, prob):
        final_prob = 0
        total_config = 0
        unmarked_states = set()
        for u in self.graph:
            for v in self.graph:
                unmarked_states.add((u,v))
                
        
        marked_states = set()
        
        
        for u in self.graph:
            unmarked_states.remove((u,u))
            marked_states.add((u,u))
            final_prob +=  prob[u]*prob[u]
            total_config += 1
    
        repeat = True
        while unmarked_states and repeat:
            repeat = False
            for c in self.graph:
                for r in self.graph:
                    if c != r and (c,r) not in marked_states:
                        for r_p in [n for n in self.graph[r]]:
                            for c_p in [n for n in self.graph[c]]:
                                if (c_p, r_p) in marked_states:
                                    try:
                                        unmarked_states.remove((c,r))
                                    except:
                                        pass
                                    marked_states.add((c,r))
                                    final_prob += (prob[c] * prob[r])
                                    total_config += 1
                                    repeat = True
                                    break
                 
        
        
        
        if unmarked_states:
            return False
#        
        print(prob)
        print(total_config)
        print(unmarked_states)
        final_prob /= total_config
        return final_prob

    # displays graph and initial cop robber positions
    def display(self):
        color_map = []
        for node in self.graph:
            color_map.append('grey')   
#                 
        nx.draw(self.graph, node_color=color_map, with_labels=True)
        plt.show()
        
    
    

def generate_graph(node_count, edge_count):

    g = nx.Graph()
    
    for i in range(edge_count):
         x = random.randint (1, node_count)
         y = random.randint (1, node_count)
         if x == y: continue
         if y < x: x, y = y, x
         g.add_edge(x,y)

    return g

if __name__ == "__main__":
    
 
    probabilities = []
    values = []
    for k in range(100):
        
        graph = generate_graph(10, 14)
        env = Environment(1, 1, graph)
        
        env.display()
        
        # baseline
#        print(env.marking()) 
        
        # extension 1
        prob = [random.randint(k,100)/100 for i in range(10)]
        probabilities.append(sum(prob)/len(prob))
        prob.insert(0, 0)
        
        val = env.marking(prob)
        print(val)
        values.append(val)
    
    plt.scatter(probabilities, values)
    plt.xlabel("Average Visibility (confidence at each node)")
    plt.ylabel("Correctness Metric")
    

