

from collections import defaultdict, deque

def generate_kmers(reads, k):
    """Generate k-mers from a list of reads."""
    for read in reads:
        for i in range(len(read) - k + 1):
            yield read[i:i + k]

def build_de_bruijn_graph(kmers):
    """Build the De Bruijn graph as an adjacency list."""
    graph = defaultdict(list)
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
    return graph

def find_eulerian_path(graph):
    """Find an Eulerian path in the graph."""
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    # Calculate in-degree and out-degree
    for node, neighbors in graph.items():
        out_degree[node] += len(neighbors)
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    # Identify start and end nodes
    start_node = None
    end_node = None
    for node in set(in_degree) | set(out_degree):
        if out_degree[node] > in_degree[node]:
            start_node = node
        elif in_degree[node] > out_degree[node]:
            end_node = node
    
    # If there's an end node, add a temporary edge for Eulerian cycle
    if end_node:
        graph[end_node].append(start_node)
    
    # Hierholzer's algorithm for Eulerian path/cycle
    stack = [start_node]
    path = deque()
    while stack:
        node = stack[-1]
        if graph[node]:
            next_node = graph[node].pop()
            stack.append(next_node)
        else:
            path.appendleft(stack.pop())
    
    # Remove the temporary edge
    if end_node:
        path = deque(node for node in path if node != start_node or node != end_node)
    
    return list(path)

def assemble_genome(path):
    """Assemble genome sequence from an Eulerian path."""
    genome = path[0]
    for node in path[1:]:
        genome += node[-1]
    return genome

# Example usage
reads = ['GCT', 'CTG', 'TGA', 'GAC', 'ACT', 'CTT', 'TTA', 'TAG', 'AGA', 'GAG']

k = 3

# Step 1: Generate k-mers
kmers = list(generate_kmers(reads, k))

# Step 2: Build the De Bruijn graph
graph = build_de_bruijn_graph(kmers)

# Step 3: Find Eulerian path
eulerian_path = find_eulerian_path(graph)

# Step 4: Assemble genome
genome = assemble_genome(eulerian_path)
print("Assembled Genome:", genome)
