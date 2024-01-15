import tkinter as tk

# unit converter function
def fahrenheit_to_celsius():
    try:
        # convert value for fahrenheit to celsius and insert into lbl_result
        fahrenheit = ent_temperature.get()
        celsius = (5 / 9) * (float(fahrenheit) - 32)
        lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    except ValueError:
        # handle case where input is not a valid float
        lbl_result["text"] = "Invalid input. Please enter a valid number!"


# create a window object
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# entry frame
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# button converter
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# layout
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

#run application
window.mainloop()