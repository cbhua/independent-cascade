def data_load(path):
    '''Load data from path
    Args: 
        path (str): path to data files;
    '''
    nodes = []
    edges = []
    file = open(path)
    for line in file:
        source, target = line.split('\t')
        nodes.append(int(source))
        nodes.append(int(target))
        edges.append((int(source), int(target)))
    nodes = list(set(nodes))
    num_nodes = len(nodes)
    num_edges = len(edges)
    print('Number of Nodes: {}'.format(num_nodes))
    print('Number of Edges: {}'.format(num_edges))
    return nodes, edges
