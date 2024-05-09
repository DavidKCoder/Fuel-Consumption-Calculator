# # Python code for the mini GUI app
# import tkinter as tk
#
# def calculate_consumption():
#     distance = float(entry_distance.get())
#     fuel = float(entry_fuel.get())
#     consumption = (fuel / distance) * 100
#     label_result.config(text=f"Fuel consumption per 100km: {consumption:.2f} liters")
#
# # Create GUI window
# window = tk.Tk()
# window.title("Fuel Consumption Calculator")
#
# # Create input fields
# label_distance = tk.Label(window, text="Distance (km):")
# label_distance.grid(row=0, column=0)
# entry_distance = tk.Entry(window)
# entry_distance.grid(row=0, column=1)
#
# label_fuel = tk.Label(window, text="Fuel consumed (liters):")
# label_fuel.grid(row=1, column=0)
# entry_fuel = tk.Entry(window)
# entry_fuel.grid(row=1, column=1)
#
# # Create button to calculate consumption
# button_calculate = tk.Button(window, text="Calculate", command=calculate_consumption)
# button_calculate.grid(row=2, columnspan=2)
#
# # Create label to display result
# label_result = tk.Label(window, text="")
# label_result.grid(row=3, columnspan=2)
#
# # Run the GUI application
# window.mainloop()
