import math
import tkinter as tk
from money import calculate_sales_needed

def calculate_sales():

     # Reset the result_label text to clear previous results
    result_label.config(text="Calculating...")
    
    # Get user input from the Entry widgets
    target_earnings = float(target_earnings_entry.get())
    cancellation_rate = float(cancellation_rate_entry.get())
    avg_contract_value = float(avg_contract_value_entry.get())

    selected_payscale = rookie_payscale if payscale_choice.get() == "Rookie" else experienced_payscale
    
    # Call your calculate_sales_needed function to calculate the result
    result = calculate_sales_needed(selected_payscale, target_earnings, cancellation_rate, avg_contract_value)
    
    # Display the result in a Label widget
    result_label.config(text=f"Total Sales Needed: {result}")

# Create a Tkinter window
root = tk.Tk()
root.title("Sales Calculator")
root.geometry("400x300")

# Create and arrange widgets
tk.Label(root, text="Select Payscale:").pack()
payscale_choice = tk.StringVar()
payscale_choice.set("Rookie")  # Set a default choice
payscale_menu = tk.OptionMenu(root, payscale_choice, "Rookie", "Experienced")
payscale_menu.pack()

# Create and arrange Entry widgets and labels
tk.Label(root, text="Target Earnings:").pack()
target_earnings_entry = tk.Entry(root)
target_earnings_entry.pack()

tk.Label(root, text="Cancellation Rate:").pack()
cancellation_rate_entry = tk.Entry(root)
cancellation_rate_entry.pack()

tk.Label(root, text="Average Contract Value:").pack()
avg_contract_value_entry = tk.Entry(root)
avg_contract_value_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_sales)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

rookie_payscale = [
    [0, 0.25], 
    [50, 0.27], 
    [85, 0.30],
    [115, 0.35],
    [200, 0.37],
    [250, 0.40],
    [300, 0.45],
    [350, 0.47],
    [400, 0.50]
    ]

experienced_payscale = [
    [0, 0.3], 
    [50, 0.32], 
    [85, 0.35],
    [115, 0.40],
    [200, 0.43],
    [250, 0.45],
    [300, 0.50],
    [350, 0.52],
    [400, 0.55]
    ]

root.mainloop()
