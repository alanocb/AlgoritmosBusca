import psutil
import time
import queue
import networkx as nx
import matplotlib.pyplot as plt

def a_star_search(graph, start_node, stop_node, heuristic_table, with_repeated_states=False):
    visited = set()
    priority_queue = queue.PriorityQueue()
    priority_queue.put((0, start_node))
    order = []

    while not priority_queue.empty():
        cost, node = priority_queue.get()

        if node in visited:
            continue

        order.append(node)
        visited.add(node)

        print(f"Visited node A*: {node}")

        if node == stop_node:
            return order

        for neighbor in graph[node]:
            if neighbor not in visited:
                neighbor_cost = cost + graph[node][neighbor]['weight']
                f_value = neighbor_cost + heuristic_table[neighbor]
                priority_queue.put((f_value, neighbor))

    return order


def bfs(graph, start_node, stop_node):
    visited = set()
    queue = [start_node]
    order = []

    while queue:
        node = queue.pop(0)

        if node in visited:
            continue

        print(f"Visited node bfs: {node}") 
        order.append(node)
        visited.add(node)

        if node == stop_node:
            return order

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return order



def dfs(graph, start_node, stop_node):
    visited = set()
    stack = [start_node]
    order = []

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        print(f"Visited node dfs: {node}")  # Print the visited node

        order.append(node)
        visited.add(node)

        if node == stop_node:
            return order

        neighbors = list(graph.successors(node))

        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)

    return order


def uniform_cost_search(graph, start_node, stop_node):
    visited = set()
    priority_queue = queue.PriorityQueue()
    priority_queue.put((0, start_node))
    order = {node: None for node in graph.nodes}

    while not priority_queue.empty():
        cost, node = priority_queue.get()

        if node in visited:
            continue

        visited.add(node)
        print(f"Visited node UNIcost: {node}")

        if node == stop_node:
            path = []
            while node is not None:
                path.insert(0, node)
                node = order[node]
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                neighbor_cost = cost + graph[node][neighbor]['weight']
                if order[neighbor] is None or neighbor_cost < cost:
                    order[neighbor] = node
                    priority_queue.put((neighbor_cost, neighbor))

    return []


#grafo 
G = nx.DiGraph()

G.add_edge(0, 2,weight=3, direction='one-way')
G.add_edge(0, 1,weight=5, direction='one-way')  

G.add_edge(1, 3,weight=4, direction='one-way')
G.add_edge(1, 4,weight=2, direction='one-way')

G.add_edge(2, 5,weight=1, direction='one-way')
G.add_edge(2, 6,weight=3, direction='one-way')

G.add_edge(3, 7,weight=2, direction='one-way')
G.add_edge(3, 8,weight=3, direction='one-way')

G.add_edge(4, 9,weight=4, direction='one-way')
G.add_edge(4, 10,weight=2, direction='one-way')

G.add_edge(5, 11,weight=1, direction='one-way')
G.add_edge(5, 12,weight=3, direction='one-way')

G.add_edge(6, 13,weight=2, direction='one-way')
G.add_edge(6, 14,weight=1, direction='one-way')

G.add_edge(7, 15,weight=2, direction='one-way')
G.add_edge(7, 16,weight=3, direction='one-way')
G.add_edge(7, 12,weight=1, direction='one-way')

G.add_edge(8, 17,weight=4, direction='one-way')
G.add_edge(8, 18,weight=2, direction='one-way')

G.add_edge(12, 7,weight=1, direction='one-way') #cria o duplo sentindo

G.add_edge(14, 12,weight=1, direction='one-way')

G.add_edge(16, 18,weight=1, direction='one-way')
pos = nx.spring_layout(G)

pos = nx.spring_layout(G)

# Tabela de valores heurísticos
heuristic_table = {
    0: 4, 1: 3, 2: 3, 3: 2, 4: 2, 5: 4, 6: 3, 7: 3, 8: 2, 9: 4,
    10: 3, 11: 2, 12: 2, 13: 4, 14: 3, 15: 3, 16: 2, 17: 4, 18: 3,
}
start_node = 0
stop_node = 18



# Function to measure memory usage
def measure_memory_usage():
    return psutil.virtual_memory().used

# Executar A* com verificação de estados repetidos
start_memory = measure_memory_usage()
start_time = time.time()
order_a_star_with_repeats = a_star_search(G, start_node, stop_node, heuristic_table, with_repeated_states=True)
a_star_with_repeats_execution_time = time.time() - start_time
end_memory = measure_memory_usage()
memory_used = end_memory - start_memory

print(f"A* com verificação de estados repetidos:")
print(f"Tempo de execução: {a_star_with_repeats_execution_time} segundos")
print(f"Memória utilizada: {memory_used} bytes\n")


# Executar A* sem verificação de estados repetidos
start_memory = measure_memory_usage()
start_time = time.time()
order_a_star_no_repeats = a_star_search(G, start_node, stop_node, heuristic_table, with_repeated_states=False)
a_star_no_repeats_execution_time = time.time() - start_time
end_memory = measure_memory_usage()
memory_used = end_memory - start_memory

print(f"A* sem verificação de estados repetidos:")
print(f"Tempo de execução: {a_star_no_repeats_execution_time} segundos")
print(f"Memória utilizada: {memory_used} bytes\n")


# Executar BFS com verificação de estados repetidos
start_memory = measure_memory_usage()
start_time = time.time()
order_bfs_with_repeats = bfs(G, start_node, stop_node)  
bfs_with_repeats_execution_time = time.time() - start_time
end_memory = measure_memory_usage()
memory_used = end_memory - start_memory

print(f"BFS com verificação de estados repetidos:")
print(f"Tempo de execução: {bfs_with_repeats_execution_time} segundos")
print(f"Memória utilizada: {memory_used} bytes\n")


# Executar BFS sem verificação de estados repetidos
start_memory = measure_memory_usage()
start_time = time.time()
order_bfs_no_repeats = bfs(G, start_node, stop_node)  
bfs_no_repeats_execution_time = time.time() - start_time
end_memory = measure_memory_usage()
memory_used = end_memory - start_memory

print(f"BFS sem verificação de estados repetidos:")
print(f"Tempo de execução: {bfs_no_repeats_execution_time} segundos")
print(f"Memória utilizada: {memory_used} bytes\n")


# Executar DFS com verificação de estados repetidos
start_memory = measure_memory_usage()
start_time = time.time()
order_dfs_with_repeats = dfs(G, start_node, stop_node) 
dfs_with_repeats_execution_time = time.time() - start_time
end_memory = measure_memory_usage()
memory_used = end_memory - start_memory

print(f"DFS com verificação de estados repetidos:")
print(f"Tempo de execução: {dfs_with_repeats_execution_time} segundos")
print(f"Memória utilizada: {memory_used} bytes\n")


# Executar DFS sem verificação de estados repetidos
start_memory = measure_memory_usage()
start_time = time.time()
order_dfs_no_repeats = dfs(G, start_node, stop_node)  
dfs_no_repeats_execution_time = time.time() - start_time
end_memory = measure_memory_usage()
memory_used = end_memory - start_memory

print(f"DFS sem verificação de estados repetidos:")
print(f"Tempo de execução: {dfs_no_repeats_execution_time} segundos")
print(f"Memória utilizada: {memory_used} bytes\n")


# Executar UCS com verificação de estados repetidos
start_memory = measure_memory_usage()
start_time = time.time()
order_ucs_with_repeats = uniform_cost_search(G, start_node, stop_node)
ucs_with_repeats_execution_time = time.time() - start_time
end_memory = measure_memory_usage()
memory_used = end_memory - start_memory

print(f"UCS com verificação de estados repetidos:")
print(f"Tempo de execução: {ucs_with_repeats_execution_time} segundos")
print(f"Memória utilizada: {memory_used} bytes\n")


# Executar UCS sem verificação de estados repetidos
start_memory = measure_memory_usage()
start_time = time.time()
order_ucs_no_repeats = uniform_cost_search(G, start_node, stop_node)
ucs_no_repeats_execution_time = time.time() - start_time
end_memory = measure_memory_usage()
memory_used = end_memory - start_memory

print(f"UCS sem verificação de estados repetidos:")
print(f"Tempo de execução: {ucs_no_repeats_execution_time} segundos")
print(f"Memória utilizada: {memory_used} bytes\n")
