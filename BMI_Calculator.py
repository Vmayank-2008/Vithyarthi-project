import tkinter as tk
from tkinter import messagebox
def calculate_bmi():
    try:
        height_cm = float(entry_height.get())
        weight_kg = float(entry_weight.get())
        if height_cm <= 0 or weight_kg <= 0:
            messagebox.showerror("Invalid input", "Height and weight must be positive values.")
            return
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        bmi_rounded = round(bmi, 2)
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        label_result.config(text=f"BMI: {bmi_rounded} - {category}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numeric values for height and weight.")
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")
label_height = tk.Label(root, text="Height (cm):")
label_height.pack(pady=(20, 5))
entry_height = tk.Entry(root)
entry_height.pack()
label_weight = tk.Label(root, text="Weight (kg):")
label_weight.pack(pady=(10, 5))
entry_weight = tk.Entry(root)
entry_weight.pack()
button_calc = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
button_calc.pack(pady=15)
label_result = tk.Label(root, text="")
label_result.pack()
root.mainloop()
