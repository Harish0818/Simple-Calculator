#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        choice = operation_var.get()

        if choice == 1:
            result = num1 + num2
        elif choice == 2:
            result = num1 - num2
        elif choice == 3:
            result = num1 * num2
        elif choice == 4:
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"
        else:
            result = "Invalid input"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

#Mmain window creation
window = tk.Tk()
window.title("Simple Calculator")

# User input box
entry_num1 = tk.Entry(window, width=15)  # Increased width
entry_num2 = tk.Entry(window, width=15)  # Increased width

# Radio buttons options
operation_var = tk.IntVar()
addition_radio = tk.Radiobutton(window, text="Addition", variable=operation_var, value=1)
subtraction_radio = tk.Radiobutton(window, text="Subtraction", variable=operation_var, value=2)
multiplication_radio = tk.Radiobutton(window, text="Multiplication", variable=operation_var, value=3)
division_radio = tk.Radiobutton(window, text="Division", variable=operation_var, value=4)

# Button to perform calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)

# Label to display the result
result_label = tk.Label(window, text="Result: ")

#  layout
entry_num1.grid(row=0, column=0, padx=10, pady=10)  
entry_num2.grid(row=0, column=1, padx=10, pady=10)  
addition_radio.grid(row=1, column=0, padx=10, pady=5)  
subtraction_radio.grid(row=1, column=1, padx=10, pady=5)  
multiplication_radio.grid(row=2, column=0, padx=10, pady=5)  
division_radio.grid(row=2, column=1, padx=10, pady=5)  
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)  
result_label.grid(row=4, column=0, columnspan=2, pady=10)  

# Start the main event loop
window.mainloop()


# In[ ]:





# In[ ]:




