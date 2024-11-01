import heapq

def dijkstra(graph, start, end):
    # Menyimpan jarak terpendek dari titik awal ke semua titik
    shortest_paths = {node: (None, float('inf')) for node in graph}
    shortest_paths[start] = (None, 0)
    
    # Menyimpan antrian prioritas
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak saat ini lebih besar dari jarak terpendek yang sudah ditemukan, lewati
        if current_distance > shortest_paths[current_node][1]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika jarak baru lebih pendek, perbarui jarak terpendek
            if distance < shortest_paths[neighbor][1]:
                shortest_paths[neighbor] = (current_node, distance)
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Membangun jalur terpendek
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = shortest_paths[current_node][0]
    path = path[::-1]  # Balik urutan jalur
    
    total_cost = shortest_paths[end][1]
    
    return path, total_cost

# Contoh graf
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
end_node = 'D'
shortest_path, total_cost = dijkstra(graph, start_node, end_node)

print(f"Jalur terpendek dari {start_node} ke {end_node}: {' -> '.join(shortest_path)}")
print(f"Biaya total: {total_cost}")
