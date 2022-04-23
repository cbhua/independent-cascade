import numpy as np


def influence_count(nodes, edges, seeds, threshold):
    ''' Calculate influent result
    Args:
        nodes (list) [#node]: nodes list of the graph;
        edges (list of list) [#edge, 2]: edges list of the graph;
        seeds (list) [#seed]: selected seeds;
        threshold (float): influent threshold, between 0 and 1;
    Return:
        final_actived_node (list): list of influent nodes;
    '''
    in_degree = {}
    inactive_nodes = []
    active_nodes = []
    nodes_status = {}

    for edge in edges: 
        if edge[0] in seeds:
            active_nodes.append(edge[0])
        else:
            inactive_nodes.append(edge[0])
        if edge[1] in seeds:
            active_nodes.append(edge[1])
        else:
            inactive_nodes.append(edge[1])
        if edge[1] in in_degree:
            in_degree[edge[1]] += 1
        else:
            in_degree[edge[1]] = 1

    active_nodes = list(set(active_nodes))
    inactive_nodes = list(set(inactive_nodes))

    for node in nodes:
        nodes_status[node] = 0
    for node in active_nodes:
        nodes_status[node] = 1
            
    while(active_nodes):
        new_actived_nodes = []
        for edge in edges:
            if nodes_status[edge[0]] == 1:
                if nodes_status[edge[1]] == 0:
                    p = np.array([1 - threshold / in_degree[edge[1]], threshold / in_degree[edge[1]]])
                    flag = np.random.choice([0, 1], p=p.ravel())
                    if flag:
                        new_actived_nodes.append(edge[1])
        for node in active_nodes:
            nodes_status[node] = 2
        for node in new_actived_nodes:
            nodes_status[node] = 1
        active_nodes = new_actived_nodes

    final_actived_node = 0
    for node in nodes:
        if nodes_status[node] == 2:
            final_actived_node += 1
    return final_actived_node  
