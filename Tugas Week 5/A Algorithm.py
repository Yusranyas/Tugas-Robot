import heapq

def heuristic(a, b):
    """Menghitung jarak Manhattan antara dua titik a dan b."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    """Implementasi algoritma A* untuk menemukan jalur terpendek di dalam grid."""
    
    # Mendapatkan ukuran grid
    rows, cols = len(grid), len(grid[0])
    
    # Antrian prioritas untuk menyimpan node yang akan dieksplorasi
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # Menyimpan biaya dari start ke node saat ini
    g_costs = {start: 0}
    
    # Menyimpan node yang telah dikunjungi
    came_from = {}
    
    while open_set:
        current_f_cost, current = heapq.heappop(open_set)
        
        # Jika kita telah mencapai tujuan, membangun jalur
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Balik urutan jalur

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # (kanan, bawah, kiri, atas)
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            # Memastikan neighbor ada dalam grid dan bukan rintangan
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                # Hitung biaya dari start ke neighbor
                tentative_g_cost = g_costs[current] + 1
                
                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    # Simpan biaya dan asal dari neighbor
                    g_costs[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + heuristic(neighbor, goal)
                    came_from[neighbor] = current
                    
                    # Tambahkan neighbor ke antrian prioritas jika belum ada
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_cost, neighbor))
    
    return None  # Jika tidak ada jalur yang ditemukan

# Contoh grid (0 = kosong, 1 = rintangan)
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)  # Titik awal
goal = (4, 4)   # Titik tujuan

path = a_star(grid, start, goal)

if path:
    print(f"Jalur yang ditemukan: {path}")
else:
    print("Tidak ada jalur yang ditemukan.")
