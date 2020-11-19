import numpy as np


def degree(edges, n):
    degree = {}
    seeds = []

    for edge in edges: 
        if edge[0] in degree:
            degree[edge[0]] += 1
        else:
            degree[edge[0]] = 1
        if edge[1] in degree:
            degree[edge[1]] += 1
        else:
            degree[edge[1]] = 1

    seeds = list({k: v for k, v in sorted(degree.items(), key=lambda item: item[1], reverse=True)}.keys())[:n]

    return seeds


def random(nodes, n):
    np.random.shuffle(nodes)
    
    return nodes[:n]


def degree_discount(edges, n):
    out_degree = {}
    connection = {}
    seeds = []

    for edge in edges:
        if edge[1] in connection:
            connection[edge[1]].append(edge[0])
        else:
            connection[edge[1]] = [edge[0]]

        if edge[0] in out_degree:
            out_degree[edge[0]] += 1
        else:
            out_degree[edge[0]] = 1

    while len(seeds) < n:
        seed = sorted(out_degree.items(), key=lambda item: item[1], reverse=True)[0][0]
        seeds.append(seed)

        out_degree[seed] = -1
        for node in connection[seed]:
            out_degree[node] -= 1
    
    return seeds


def degree_neighbor(edges, n):
    out_degree = {}
    centrality_score = {}
    seeds = []

    for edge in edges:
        if edge[0] in out_degree:
            out_degree[edge[0]] += 1
        else:
            out_degree[edge[0]] = 1

    centrality_score = out_degree.copy()

    for edge in edges:
        if edge[1] in out_degree:
            centrality_score[edge[0]] += out_degree[edge[1]]
        else:
            pass

    seeds = list({k: v for k, v in sorted(centrality_score.items(), key=lambda item: item[1], reverse=True)}.keys())[:n]

    return seeds


def degree_neighbor_fix(edges, n):
    out_degree = {}
    centrality_score = {}
    connection = {}
    seeds = []

    for edge in edges:
        if edge[1] in connection:
            connection[edge[1]].append(edge[0])
        else:
            connection[edge[1]] = [edge[0]]

        if edge[0] in out_degree:
            out_degree[edge[0]] += 1
        else:
            out_degree[edge[0]] = 1

    centrality_score = out_degree.copy()

    for edge in edges:
        if edge[1] in out_degree:
            centrality_score[edge[0]] += out_degree[edge[1]]
        else:
            pass

    while len(seeds) < n:
        seed = sorted(centrality_score.items(), key=lambda item: item[1], reverse=True)[0][0]
        seeds.append(seed)
        centrality_score[seed] = -1
        for node in connection[seed]:
            centrality_score[node] -= out_degree[seed]

    return seeds


def mia(nodes, edges, n):
    theta = 0.1
    nodes = []
    out_connection = {}
    centrality_score = {}
    seeds = []

    for edge in edges:
        if edge[0] in out_connection:
            out_connection[edge[0]].append(edge[1])
        else:
            out_connection[edge[0]] = [edge[1]]

    for node in nodes:
        centrality_score[node] = mia_centrality(node, out_connection, 0, ap=1, theta=theta)

    i = 0
    centrality_score = {k: v for k, v in sorted(centrality_score.items(), key=lambda item: item[0])}
    for node, score in sorted(centrality_score.items(), key=lambda item: item[1], reverse=True):
        if i >= n:
            break
        else:
            i += 1
        seeds.append(node)
    
    return seeds


def mia_centrality(node, out_connection, centrality_score, ap, theta):
    if node not in out_connection.keys():
        return 1
    
    ap *= 1 / len(out_connection[node])
    if ap < theta:
        return 1
    
    for sub_node in out_connection[node]:
        centrality_score += mia_centrality(sub_node, out_connection, centrality_score, ap, theta)
    
    return centrality_score