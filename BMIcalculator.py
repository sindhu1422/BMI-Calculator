import tkinter as tk

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("350x300")

tk.Label(window, text="BMI Calculator").pack(pady=10)

tk.Label(window, text="Enter weight in kg").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Label(window, text="Enter height in meters").pack()
height_entry = tk.Entry(window)
height_entry.pack()
def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    result.config(text="BMI = " + str(round(bmi, 2)) + "\n" + category)

button = tk.Button(window, text="Calculate", command=calculate_bmi)
button.pack(pady=10)

result = tk.Label(window, text="")
result.pack()
window.mainloop()