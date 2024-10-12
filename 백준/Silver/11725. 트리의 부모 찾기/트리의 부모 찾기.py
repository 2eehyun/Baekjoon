N = int(input())
link_arr = [[] for _ in range(N+1)]
parents = [0]*(N+1)

for _ in range(N-1):
    node1, node2 = map(int, input().split())
    link_arr[node1].append(node2)
    link_arr[node2].append(node1)

stack = [1]
while stack:
    parent_node = stack.pop()
    temp_childs = []
    for child_node in link_arr[parent_node]:
        temp_childs.append(child_node)
        stack.append(child_node)
        parents[child_node] = parent_node
    for child_node in temp_childs:
        link_arr[parent_node].remove(child_node)
        link_arr[child_node].remove(parent_node)

for node in range(2, N+1):
    print(parents[node])