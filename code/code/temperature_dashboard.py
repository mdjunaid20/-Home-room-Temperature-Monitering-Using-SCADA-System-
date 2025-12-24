import serial
import time
import matplotlib.pyplot as plt
from collections import deque

# ---------------- SETTINGS ----------------
PORT = "COM3"   # Change this to your Arduino port
BAUD = 9600
LIMIT_LOW = 18
LIMIT_HIGH = 30
MAX_POINTS = 50  # Number of points to show on the graph
# ------------------------------------------

# Connect to Arduino via serial
ser = serial.Serial(PORT, BAUD)
time.sleep(2)  # wait for Arduino to initialize

# Queue to store temperature points
temps = deque(maxlen=MAX_POINTS)

# Set up live plot
plt.ion()
fig, ax = plt.subplots()

while True:
    data = ser.readline().decode().strip()

    try:
        temp = float(data)
        temps.append(temp)

        ax.clear()
        ax.plot(list(temps), marker='o')
        ax.set_ylim(10, 40)
        ax.set_title("Room Temperature Monitoring (SCADA Style)")
        ax.set_ylabel("Temperature (°C)")
        ax.set_xlabel("Time (latest points)")

        # Alert messages
        if temp < LIMIT_LOW:
            print(f"LOW TEMP ALERT! {temp} °C")
        elif temp > LIMIT_HIGH:
            print(f"HIGH TEMP ALERT! {temp} °C")
        else:
            print(f"Temperature: {temp} °C")

        plt.pause(0.1)  # update the plot

    except ValueError:
        # Ignore any lines that cannot be converted to float
        pass
