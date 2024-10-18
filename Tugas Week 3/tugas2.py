from controller import Robot

# Inisialisasi robot
robot = Robot()

# Waktu langkah simulasi (ms)
time_step = 64

# Inisialisasi motor
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Atur mode posisi motor menjadi tidak terbatas (infinity)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Atur kecepatan motor
left_motor.setVelocity(2.0)  # Kecepatan roda kiri lebih lambat
right_motor.setVelocity(4.0)  # Kecepatan roda kanan lebih cepat

# Simulasi berjalan terus-menerus
while robot.step(time_step) != -1:
    # Simulasi loop
    pass