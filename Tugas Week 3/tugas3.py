from controller import Robot

# Inisialisasi robot
robot = Robot()

# Waktu sampling untuk Webots
timestep = int(robot.getBasicTimeStep())

# Mendefinisikan sensor proximity dan motor
proximity_sensors = []
for i in range(8):
    sensor = robot.getDevice(f'ps{i}')
    sensor.enable(timestep)
    proximity_sensors.append(sensor)

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Mengatur mode motor menjadi velocity control
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Fungsi untuk menghentikan robot
def stop_robot():
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

# Fungsi untuk menggerakkan robot maju
def move_forward(speed):
    left_motor.setVelocity(speed)
    right_motor.setVelocity(speed)

# Simulasi utama
while robot.step(timestep) != -1:
    # Membaca data dari sensor proximity di depan (sensor 0 dan 7)
    front_left_value = proximity_sensors[0].getValue()
    front_right_value = proximity_sensors[7].getValue()

    # Jika ada objek di depan (threshold dapat disesuaikan)
    if front_left_value > 80 or front_right_value > 80:
        stop_robot()  # Hentikan robot
    else:
        move_forward(3)  # Gerakkan robot maju dengan kecepatan 3de.
