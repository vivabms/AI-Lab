def depth_limited_search(graph, source, target, limit, visited=None):
    if visited is None:
        visited = set()
    
    if source == target:
        return True
    
    if limit <= 0:
        return False
    
    visited.add(source)
    for neighbor in graph.get(source, []):
        if neighbor not in visited:
            if depth_limited_search(graph, neighbor, target, limit - 1, visited):
                return True
    return False

def iterative_deepening_search(graph, source, target, max_depth):
    for limit in range(max_depth + 1):
        print(f"Searching with depth limit: {limit}")
        visited = set()
        if depth_limited_search(graph, source, target, limit, visited):
            return True
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

target_node = 'F'
max_depth_limit = 3
print(f"Searching for target node '{target_node}' starting from 'A':")
found = iterative_deepening_search(graph, 'A', target_node, max_depth_limit)
print(f"Target found: {found}")