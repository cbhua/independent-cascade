
def data_load(path):
    nodes = []
    edges = []

    file = open(path)

    for line in file:
        source, target = line.split('\t')
        nodes.append(int(source))
        nodes.append(int(target))
        edges.append((int(source), int(target)))
    
    nodes = list(set(nodes))
    data_stastics(nodes, edges)

    return nodes, edges


def data_stastics(nodes, edges):
    num_nodes = len(nodes)
    num_edges = len(edges)

    print('Number of Nodes: {}'.format(num_nodes))
    print('Number of Edges: {}'.format(num_edges))