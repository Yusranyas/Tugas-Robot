from controller import Robot

# Inisialisasi robot
robot = Robot()

# Dapatkan waktu langkah simulasi
timestep = int(robot.getBasicTimeStep())

# Ambil referensi ke motor roda
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set mode motor ke 'velocity' untuk mengatur kecepatan
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Kecepatan maju konstan untuk kedua roda
speed = 3.0

# Atur kecepatan motor
left_motor.setVelocity(speed)
right_motor.setVelocity(speed)

# Loop simulasi
while robot.step(timestep) != -1:
    pass  # Tidak ada logika tambahan, robot terus maju
