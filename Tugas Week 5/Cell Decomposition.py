from collections import deque

def bfs(grid, start, goal):
    """Menggunakan BFS untuk menemukan jalur dari start ke goal dalam grid."""
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    came_from = {start: None}
    
    while queue:
        current = queue.popleft()
        
        # Jika mencapai tujuan, bangun jalur
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Balik urutan jalur
        
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # (kanan, bawah, kiri, atas)
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                if neighbor not in came_from:  # Belum dikunjungi
                    came_from[neighbor] = current
                    queue.append(neighbor)
    
    return None  # Jika tidak ada jalur yang ditemukan

def cell_decomposition(grid, start, goal):
    """Fungsi utama untuk memecah ruang menjadi cell dan mencari jalur aman."""
    path = bfs(grid, start, goal)
    
    return path

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

path = cell_decomposition(grid, start, goal)

if path:
    print(f"Jalur yang ditempuh robot: {path}")
else:
    print("Tidak ada jalur yang ditemukan.")
