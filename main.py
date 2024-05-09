from PIL import Image
Image.CUBIC = Image.BICUBIC

import ttkbootstrap as ttk

app = ttk.Window(
    title="Fuel Consumption Calculator",
    themename="darkly",
    resizable=(False, False),
)
app.geometry('600x800')


# Function to get the value of the Entry widget
def get_consumption():
    km = kilometer_entry.get()
    liter = liter_entry.get()
    if km.isdigit() and liter.isdigit():
        if km == "0" or liter == "0":
            current_value = meter.amountusedvar.get()
            meter.step(-current_value)
        else:
            spend_liter = int((int(liter) * 100) / int(km))
            meter.step(spend_liter)


def validate_number(x) -> bool:
    if x.isdigit():
        return True
    elif x == "":
        return True
    else:
        return False


digit_func = app.register(validate_number)


label = ttk.Label(app, text="Please Enter km & liter ⛽", bootstyle="warning")
label.pack(pady=30)
label.config(font=('Consolas', 15))

kilometer_frame = ttk.Frame(app)
kilometer_frame.pack(pady=15, padx=10, fill='x')
ttk.Label(kilometer_frame, text="Distance (km):").pack()
kilometer_entry = ttk.Entry(kilometer_frame, validate="focus", validatecommand=(digit_func, '%P'))
kilometer_entry.pack(side='left', fill="x", expand=True, padx=5)

liter_frame = ttk.Frame(app)
liter_frame.pack(pady=15, padx=10, fill='x')
ttk.Label(liter_frame, text='Fuel consumed (liters):').pack()
liter_entry = ttk.Entry(liter_frame, validate="focus", validatecommand=(digit_func, '%P'))
liter_entry.pack(side='left', fill="x", expand=True, padx=5)

meter = ttk.Meter(
    app,
    bootstyle="danger",
    subtext="Per 100 km",
    metertype="semi",
    metersize=150,
    padding=50,
    amounttotal=50,
    subtextstyle="light",
    textright="liters",
)
meter.pack(pady=50)

button_frame = ttk.Frame(app)
button_frame.pack(pady=10, padx=10, fill='x')
ttk.Button(button_frame, text="Calculate", bootstyle="success", command=get_consumption).pack(side="left", padx=10)

app.mainloop()