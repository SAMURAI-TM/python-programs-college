import tkinter as tk
from tkinter import ttk, messagebox
import random

# Track current theme
is_dark_mode = False  # Global variable for theme toggle

# Function for Real-Time Unit Conversion
def real_time_conversion(*args):
    try:
        temp = float(temp_var.get())
        from_unit = from_combobox.get()
        to_unit = to_combobox.get()

        if from_unit == to_unit:
            result = f"{temp:.2f} {to_unit}"
            result_label.config(text=f"🌡️ {result}")
            add_to_history(result)
            return

        # Convert to Celsius first
        if from_unit == "Fahrenheit":
            temp = (temp - 32) * 5 / 9
        elif from_unit == "Kelvin":
            temp = temp - 273.15

        # Convert from Celsius to the desired unit
        if to_unit == "Fahrenheit":
            temp = (temp * 9 / 5) + 32
        elif to_unit == "Kelvin":
            temp = temp + 273.15

        result = f"{temp:.2f} {to_unit}"
        result_label.config(text=f"🌡️ Converted: {result}", foreground="lime")
        add_to_history(result)
    except ValueError:
        if temp_var.get():  # Only show error if input is not empty
            result_label.config(text="Invalid Input!", foreground="red")

# Function to Toggle Themes
def toggle_theme():
    global is_dark_mode
    if is_dark_mode:  # Switch to Light Theme
        root.configure(bg="#C0C0C0")
        style.configure("TLabel", foreground="white", background="#2c3e50")
        style.configure("TButton", background="#16a085", foreground="white")
        style.configure("TCombobox", foreground="black", background="white")
        history_list.configure(bg="#FCE6C9", fg="black")
        result_label.configure(background="#2c3e50")
    else:  # Switch to Dark Theme
        root.configure(bg="#2c3e50")
        style.configure("TLabel", foreground="black", background="#C0C0C0")
        style.configure("TButton", background="#FCE6C9", foreground="black")
        style.configure("TCombobox", foreground="black", background="#C0C0C0")
        history_list.configure(bg="#444444", fg="white")
        result_label.configure(background="#C0C0C0")
    is_dark_mode = not is_dark_mode

# Function to Show Temperature Facts
def show_temperature_fact():
    facts = [
        "Did you know? -40°C is the same as -40°F.",
        "Water boils at 100°C or 212°F at sea level.",
        "Absolute zero is the lowest possible temperature: -273.15°C or 0 Kelvin.",
        "Extreme temperatures above 50°C can cause heat stroke!"
    ]
    messagebox.showinfo("Fun Fact", random.choice(facts))

# Function to Add to Conversion History
def add_to_history(result):
    history_list.insert(tk.END, result)

# Create Main Window
root = tk.Tk()
root.title("🔥 ADVANCED TEMPERATURE CONVERTER 🔥")
root.geometry("800x600")
root.configure(bg="#C0C0C0")

# Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", foreground="white", background="#2c3e50", font=("Arial", 14))
style.configure("TButton", font=("Arial", 12, "bold"), padding=10, background="#16a085", foreground="white")
style.configure("TCombobox", font=("Arial", 12), padding=5)

# Temperature Input Field
temp_var = tk.StringVar()
temp_var.trace("w", real_time_conversion)  # Real-time conversion
entry_label = ttk.Label(root, text="Enter Temperature:")
entry_label.pack(pady=5)
entry = ttk.Entry(root, textvariable=temp_var, font=("Arial", 14), justify='center')
entry.pack(pady=5)

# From Unit
from_label = ttk.Label(root, text="From:")
from_label.pack()
from_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", font=("Arial", 12))
from_combobox.pack()
from_combobox.set("Celsius")

# To Unit
to_label = ttk.Label(root, text="To:")
to_label.pack()
to_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", font=("Arial", 12))
to_combobox.pack()
to_combobox.set("Fahrenheit")

# Conversion History
history_label = ttk.Label(root, text="Conversion History:")
history_label.pack(pady=5)
history_list = tk.Listbox(root, height=6, font=("Arial", 12), bg="#FCE6C9", fg="black")
history_list.pack(pady=10)

# Result Label
result_label = ttk.Label(root, text="", font=("Arial", 16, "bold"), background="#2c3e50")
result_label.pack(pady=10)

# Fact Button
fact_button = ttk.Button(root, text="Tell Me a Temperature Fact", command=show_temperature_fact, style="TButton")
fact_button.pack(pady=10)

# Theme Toggle Button
theme_button = ttk.Button(root, text="Toggle Theme", command=toggle_theme, style="TButton")
theme_button.pack(pady=10)

# Run Main Loop
root.mainloop()
