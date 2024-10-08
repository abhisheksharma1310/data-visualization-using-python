import serial
import time
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialize Serial Communication
arduino = serial.Serial(port='COM15', baudrate=9600, timeout=1)  # Adjust 'COM15' as needed
time.sleep(2)

# Function to send commands to Arduino
def send_command(command):
    arduino.write(f"{command}\n".encode())

# Function to update sensor data
def update_data():
    send_command('READ_TEMP')
    data = arduino.readline().decode('utf-8').strip()
    if "Temperature" in data:
        temp_value = float(data.split(": ")[1].replace("C", ""))
        temperature_data.append(temp_value)
        time_data.append(time.time() - start_time)
        update_plot()
        temp_label.config(text=f"Current Temperature: {temp_value} °C")
    root.after(1000, update_data)

# Function to update the plot
def update_plot():
    ax.clear()
    ax.plot(time_data, temperature_data, marker='o', color='b')
    ax.set_title("Real-Time Temperature Data")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    canvas.draw()

# GUI Setup
root = tk.Tk()
root.title("Arduino Control Panel with Data Visualization")

# Buttons to control the LED
btn_led_on = tk.Button(root, text="Turn On LED", command=lambda: send_command('LED_ON'))
btn_led_on.pack(pady=10)

btn_led_off = tk.Button(root, text="Turn Off LED", command=lambda: send_command('LED_OFF'))
btn_led_off.pack(pady=10)

# Label to display temperature
temp_label = tk.Label(root, text="Current Temperature: -- °C")
temp_label.pack(pady=20)

# Setting up Matplotlib Figure for Real-Time Plotting
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
temperature_data = []
time_data = []
start_time = time.time()

# Embedding the Matplotlib Figure in Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Start updating data and running GUI
root.after(1000, update_data)
root.mainloop()