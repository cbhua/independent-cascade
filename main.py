import argparse
import data_process
import seeds_selection
import influence_count

parser = argparse.ArgumentParser()

parser.add_argument('path', help='path of the graph dataset file')
parser.add_argument('-p', '--policy', default='degree', help='seeds selection policy')
parser.add_argument('-t', '--threshold', type=float, default=1, help='propagation threshold1')
parser.add_argument('-r', '--init_rate', type=float, default=0.01, help='initial rate of active nodes')

args = parser.parse_args()

print('Loading Data...')
nodes, edges = data_process.data_load(args.path)
print('Done')

print('Generating Seeds...')
seeds_number = int(len(nodes) * args.init_rate)
if args.policy == 'degree':
    seeds = seeds_selection.degree(edges, seeds_number)
elif args.policy == 'random':
    seeds = seeds_selection.random(nodes, seeds_number)
elif args.policy == 'degree_discount':
    seeds = seeds_selection.degree_discount(edges, seeds_number)
elif args.policy == 'degree_neighbor':
    seeds = seeds_selection.degree_neighbor(edges, seeds_number)
elif args.policy == 'degree_neighbor_fix':
    seeds = seeds_selection.degree_neighbor_fix(edges, seeds_number)
else:
    seeds = seeds_selection.mia(nodes, edges, seeds_number)
print('Done')

print('Calculating Influence Number...')
influence_number = influence_count.influence_count(nodes, edges, seeds, args.threshold)
print('Done')

print('Final Influenced Number: {}'.format(influence_number))