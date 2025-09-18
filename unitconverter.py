from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from unitconvert import (lengthunits, volumeunits, massunits, digitalunits, timeunits, temperatureunits)

# Creating Window
root = Tk()
root.title("Unit Converter Application")
root.geometry("1000x600")
root.resizable(False, False)
root.configure(padx=20, pady=20)

# Background Image
bg_image = Image.open("bg1.png")
bg_image = bg_image.resize((1000, 600))
bg_image = ImageTk.PhotoImage(bg_image)
canvas = Canvas(root, width=1000, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Creating Variables
user_input_value = DoubleVar()
user_input_value.set("")
output_label_value = DoubleVar()
unit_button_value = StringVar()
from_combobox_value = StringVar()
to_combobox_value = StringVar()

def update_selected_unit_label(unit):
    display_label.config(text=unit)

def on_unit_button_click(unit):
    unit_button_value.set(unit)
    update_selected_unit_label(unit)
    update_combobox_values(unit)

def update_combobox_values(unit):
    if unit == "Length":
        values = ("mm", "cm", "in", "ft", "yd", "m", "km", "mi")
    elif unit == "Volume":
        values = ("ml", "l", "tsp", "tbsp", "floz", "cup", "pt", "qt", "gal", "lcup", "in3", "ft3")
    elif unit == "Mass":
        values = ("mg", "g", "oz", "lb", "kg")
    elif unit == "Time":
        values = ("ms", "sec", "min", "hr", "day", "wk", "mo", "yr")
    elif unit == "Digital":
        values = ("B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
    elif unit == "Temperature":
        values = ("F", "C", "K")
    from_combobox['values'] = values
    to_combobox['values'] = values

def convert():
    try:
        unit_to_convert = unit_button_value.get()
        from_unit = from_combobox_value.get()
        to_unit = to_combobox_value.get()
        value_to_convert = user_input_value.get()

        if unit_to_convert == "Length":
            result = lengthunits.LengthUnit(value_to_convert, from_unit, to_unit).doconvert()
        elif unit_to_convert == "Volume":
            result = volumeunits.VolumeUnit(value_to_convert, from_unit, to_unit).doconvert()
        elif unit_to_convert == "Mass":
            result = massunits.MassUnit(value_to_convert, from_unit, to_unit).doconvert()
        elif unit_to_convert == "Time":
            result = timeunits.TimeUnit(value_to_convert, from_unit, to_unit).doconvert()
        elif unit_to_convert == "Digital":
            result = digitalunits.DigitalUnit(value_to_convert, from_unit, to_unit).doconvert()
        elif unit_to_convert == "Temperature":
            result = temperatureunits.TemperatureUnit(value_to_convert, from_unit, to_unit).doconvert()

        output_label_value.set(result)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def reset():
    user_input_value.set("")
    output_label_value.set(0)

def resetall():
    user_input_value.set("")
    output_label_value.set(0)
    display_label.config(text="Selected Unit")
    from_combobox.set("From")
    to_combobox.set("To")

def selected(event):
    unit_label = event.widget.get()
    update_combobox_values(unit_label)

# Creating image buttons for selecting unit
unit_buttons = {
    "Length": "Length.png",
    "Volume": "Volume.png",
    "Mass": "Mass.png",
    "Time": "Time.png",
    "Digital": "Digital.png",
    "Temperature": "Temperature.png",
}

unit_button_images = {}
x = 20
y = 200

for unit, image_path in unit_buttons.items():
    image = Image.open(image_path)
    image = image.resize((100, 80))
    unit_button_images[unit] = ImageTk.PhotoImage(image)
    button = Button(canvas, image=unit_button_images[unit], command=lambda unit=unit: on_unit_button_click(unit))
    button.place(x=x, y=y)
    x += 120
    if x > 340:
        x = 20
        y += 100

# Labels
unit_label = Label(root, text="Select Unit:", font="Helvetica 18 bold", bg="white")
unit_label.place(x=500, y=150)

display_label = Label(root, text="Selected Unit", font="TimeNewRoman 18 bold", bg="white")
display_label.place(x=500, y=200)

from_label = Label(root, text="From:", font="Helvetica 18 bold", bg="white")
from_label.place(x=500, y=250)

to_label = Label(root, text="To:", font="Helvetica 18 bold", bg="white")
to_label.place(x=500, y=300)

value_label = Label(root, text="Value:", font="Helvetica 18 bold", bg="white")
value_label.place(x=500, y=350)

display_output_label = Label(root, text="Output:", font="TimeNewRoman 18 bold", bg="white")
display_output_label.place(x=500, y=400)

main_label = Label(root, text="Unit Converter Application ", font="TimesNewRoman 30 bold", bg="white")
main_label.place(x=300, y=20)

# Comboboxes
from_combobox = ttk.Combobox(root, state="readonly", textvariable=from_combobox_value, font="Helvetica 16 bold", width=5)
from_combobox.set("select unit")
from_combobox.place(x=600, y=250)

to_combobox = ttk.Combobox(root, state="readonly", textvariable=to_combobox_value, font="Helvetica 16 bold", width=5)
to_combobox.set("select unit")
to_combobox.place(x=600, y=300)

# Output label
output_label = Label(root, textvariable=output_label_value, font="Helvetica 18 bold", bg="white", fg="blue")
output_label.place(x=600, y=400)

# User Input Field
user_input = Entry(root, textvariable=user_input_value, font="Helvetica 18 bold", width=10)
user_input.place(x=600, y=350)

# Creating Buttons
convert_button = Button(root, text="CONVERT", font="RobotoMono 12 bold", command=convert, padx=10, pady=5, bg="#4283f3", fg="white", activebackground="#4283f3", activeforeground="white")
convert_button.place(x=500, y=450)

reset_button = Button(root, text="RESET", font="RobotoMono 12 bold", command=reset, padx=10, pady=5, bg='#ffbd03', fg="white", activebackground='#ffbd03', activeforeground='white')
reset_button.place(x=650, y=450)

reset_all_button = Button(root, text="RESET ALL", font="RobotoMono 12 bold", command=resetall, padx=10, pady=5, bg='#FF3131', fg="white", activebackground='#FF3131', activeforeground='white')
reset_all_button.place(x=750, y=450)

# Creating Mainloop
root.mainloop()
