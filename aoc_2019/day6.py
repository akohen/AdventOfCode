def build_orbit_tree(input):
  tree = {}
  for line in input:
    bodies = line.split(')')
    if bodies[0] not in tree:
      tree[bodies[0]] = {'name': bodies[0], 'children':[], 'parent':None, 'depth': 0}
    if bodies[1] not in tree:
      tree[bodies[1]] = {'name': bodies[1], 'children':[], 'parent':tree[bodies[0]]}
    tree[bodies[0]]['children'].append(tree[bodies[1]])
    tree[bodies[1]]['parent'] = tree[bodies[0]]
  return tree

def compute_depth(node):
  for child in node['children']:
    child['depth'] = node['depth'] + 1
    compute_depth(child)

def orbit_checksum(tree):
  sum = 0
  for node in tree:
    sum += tree[node]['depth']
  return sum

def get_parent_list(node):
  if node['parent'] is None:
    return []
  return  get_parent_list(node['parent']) + [node['parent']['name']]

def find_common_parent(node1, node2):
  if node1['depth'] > node2['depth']:
    parents1 = get_parent_list(node1)
    parents2 = get_parent_list(node2)
  else:
    parents2 = get_parent_list(node1)
    parents1 = get_parent_list(node2)

  for i in range(0, len(parents2) ):
    if parents1[i] != parents2[i]:
      return i
  return i

def find_distance(node1, node2):
  common_parent = find_common_parent(node1, node2)
  return node2['depth'] + node1['depth'] - 2*common_parent

if __name__ == "__main__":
  with open('./input/day6') as f:
    tree = build_orbit_tree([line.rstrip('\n') for line in f])
    compute_depth(tree['COM'])
    print(orbit_checksum(tree))
    print(find_distance(tree['YOU'],tree['SAN']))